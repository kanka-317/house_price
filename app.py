import streamlit as st
import numpy as np
import joblib
import streamlit.components.v1 as components
import plotly.graph_objects as go

# Load model
model = joblib.load("Random_search.pkl")

# Page config
st.set_page_config(page_title="Pro House Price Predictor", layout="wide")

# ------------------ CSS ------------------
st.markdown("""
<style>
.main {background-color:#f4f6f9;}
.title {
    text-align:center;
    font-size:45px;
    font-weight:bold;
    color:#2c3e50;
}
.card {
    background:white;
    padding:25px;
    border-radius:15px;
    box-shadow:0 8px 20px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)

# ------------------ TITLE ------------------
st.markdown('<div class="title">🏠 Smart 3D Real Estate Dashboard</div>', unsafe_allow_html=True)
st.markdown("---")

# ------------------ 3D HOUSE WITH MOUSE CONTROL ------------------
components.html("""
<!DOCTYPE html>
<html>
<head>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128/examples/js/controls/OrbitControls.js"></script>
</head>
<body style="margin:0;">
<script>
let scene = new THREE.Scene();
let camera = new THREE.PerspectiveCamera(75, 600/350, 0.1, 1000);

let renderer = new THREE.WebGLRenderer({ antialias:true });
renderer.setSize(600,350);
document.body.appendChild(renderer.domElement);

// Controls (mouse interaction)
let controls = new THREE.OrbitControls(camera, renderer.domElement);

// Light
let light = new THREE.DirectionalLight(0xffffff, 1);
light.position.set(5,5,5);
scene.add(light);

// House base
let house = new THREE.Mesh(
    new THREE.BoxGeometry(2,1,2),
    new THREE.MeshStandardMaterial({color:0x8B4513})
);
scene.add(house);

// Roof
let roof = new THREE.Mesh(
    new THREE.ConeGeometry(1.5,1,4),
    new THREE.MeshStandardMaterial({color:0xff0000})
);
roof.position.y = 1;
roof.rotation.y = Math.PI/4;
scene.add(roof);

// Ground
let ground = new THREE.Mesh(
    new THREE.PlaneGeometry(10,10),
    new THREE.MeshStandardMaterial({color:0x228B22})
);
ground.rotation.x = -Math.PI/2;
ground.position.y = -1;
scene.add(ground);

camera.position.set(3,3,5);

function animate(){
    requestAnimationFrame(animate);
    controls.update();
    renderer.render(scene,camera);
}
animate();
</script>
</body>
</html>
""", height=360)

# ------------------ LAYOUT ------------------
col1, col2 = st.columns([1,1])

# ------------------ INPUT FORM ------------------
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📥 Property Details")

    bedroom = st.number_input("Bedrooms", 0, 10, 2)
    bathroom = st.number_input("Bathrooms", 0, 10, 2)
    living_area = st.number_input("Living Area (sq ft)", 500, 10000, 2000)
    condition = st.slider("Condition", 1, 5, 3)
    school = st.number_input("Nearby Schools", 0, 10, 2)

    x = [[bedroom, bathroom, living_area, condition, school]]

    if st.button("🚀 Predict Price"):
        price = int(model.predict(np.array(x))[0])
        st.success(f"💰 Predicted Price: ₹ {price:,}")

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------ 3D GRAPH ------------------
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 3D Price Visualization")

    # Sample grid
    x_range = np.linspace(500, 5000, 20)
    y_range = np.linspace(1, 5, 20)
    X, Y = np.meshgrid(x_range, y_range)

    Z = []
    for i in range(len(X)):
        row = []
        for j in range(len(X[i])):
            val = model.predict([[2,2,X[i][j],Y[i][j],2]])[0]
            row.append(val)
        Z.append(row)

    fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])

    fig.update_layout(
        scene=dict(
            xaxis_title='Living Area',
            yaxis_title='Condition',
            zaxis_title='Price'
        ),
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------ FOOTER ------------------
st.markdown("---")
st.markdown("🚀 Built with Streamlit + ML + Three.js | Portfolio Ready Project")