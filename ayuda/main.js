// Define la URL del archivo JSON
const url = 'geometries.json';

// Utiliza fetch para obtener el contenido del archivo JSON
fetch(url)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    // Crea una nueva escena de Three.js
    const scene = new THREE.Scene();

    // Recorre las geometrías en el JSON y crea cada una
    data.geometries.forEach(geometryData => {
      let geometry;

      // Según el tipo de geometría, crea la geometría correspondiente
      switch (geometryData.type) {
        case 'BoxGeometry':
          geometry = new THREE.BoxGeometry(
            geometryData.width,
            geometryData.height,
            geometryData.depth,
            geometryData.widthSegments,
            geometryData.heightSegments,
            geometryData.depthSegments
          );
          break;
        case 'CylinderGeometry':
          geometry = new THREE.CylinderGeometry(
            geometryData.radiusTop,
            geometryData.radiusBottom,
            geometryData.height,
            geometryData.radialSegments,
            geometryData.heightSegments,
            geometryData.openEnded,
            geometryData.thetaStart,
            geometryData.thetaLength
          );
          break;
        // Agrega más casos según sea necesario para otros tipos de geometrías
        default:
          console.error('Unknown geometry type:', geometryData.type);
          return;
      }

      // Crea un material para la geometría (en este caso, un material básico)
      const material = new THREE.MeshBasicMaterial({ color: 0xff0000 });

      // Crea una malla (mesh) usando la geometría y el material
      const mesh = new THREE.Mesh(geometry, material);

      // Asigna el nombre de la geometría al objeto mesh
      mesh.name = geometryData.name;

      // Añade la malla a la escena
      scene.add(mesh);
    });

    // Agrega geometrías adicionales
    const additionalGeometries = [
        {
			"uuid": "3bff4024-39ab-4875-bce1-bc8f6978f1cf",
			"type": "BoxGeometry",
			"name": "palo1",
			"width": 1,
			"height": 1,
			"depth": 1,
			"widthSegments": 1,
			"heightSegments": 1,
			"depthSegments": 1
		},
		{
			"uuid": "6d8cd110-50fa-4e85-80be-9eb5b51324eb",
			"type": "BoxGeometry",
			"name": "base2",
			"width": 1,
			"height": 1,
			"depth": 1,
			"widthSegments": 1,
			"heightSegments": 1,
			"depthSegments": 1
		},
		{
			"uuid": "6221cd24-23de-4114-8ee3-ccb7333452b9",
			"type": "BoxGeometry",
			"name": "base1",
			"width": 1,
			"height": 1,
			"depth": 1,
			"widthSegments": 1,
			"heightSegments": 1,
			"depthSegments": 1
		},
		{
			"uuid": "3432b7b7-8234-4398-95a7-19855cd40a33",
			"type": "BoxGeometry",
			"name": "base 3",
			"width": 1,
			"height": 1,
			"depth": 1,
			"widthSegments": 1,
			"heightSegments": 1,
			"depthSegments": 1
		},
		{
			"uuid": "8e0b0115-5e99-482d-99d6-1a145b8c4c14",
			"type": "BoxGeometry",
			"name": "base 4",
			"width": 1,
			"height": 1,
			"depth": 1,
			"widthSegments": 1,
			"heightSegments": 1,
			"depthSegments": 1
		},
		{
			"uuid": "57054775-f8c6-490c-b475-a2c399a1a303",
			"type": "BoxGeometry",
			"name": "piso",
			"width": 1,
			"height": 1,
			"depth": 1,
			"widthSegments": 1,
			"heightSegments": 1,
			"depthSegments": 1
		},
		{
			"uuid": "d502afed-85ea-4892-851a-d1b8b164f372",
			"type": "BoxGeometry",
			"name": "palo2",
			"width": 1,
			"height": 1,
			"depth": 1,
			"widthSegments": 1,
			"heightSegments": 1,
			"depthSegments": 1
		},
		{
			"uuid": "a1d4d830-465b-4bc0-a1d6-008043ac3f62",
			"type": "BoxGeometry",
			"name": "parteunion",
			"width": 1,
			"height": 1,
			"depth": 1,
			"widthSegments": 1,
			"heightSegments": 1,
			"depthSegments": 1
		},
		{
			"uuid": "79f5214f-98fa-4747-8033-74c86d9b7939",
			"type": "BoxGeometry",
			"width": 1,
			"height": 1,
			"depth": 1,
			"widthSegments": 1,
			"heightSegments": 1,
			"depthSegments": 1
		},
		{
			"uuid": "cefd6bb0-37b6-45dc-aaf0-9d79b5eae7fe",
			"type": "BoxGeometry",
			"width": 1,
			"height": 1,
			"depth": 1,
			"widthSegments": 1,
			"heightSegments": 1,
			"depthSegments": 1
		},
		{
			"uuid": "e251a61e-58fc-4b32-bb4a-0c7173ee877a",
			"type": "BoxGeometry",
			"width": 1,
			"height": 1,
			"depth": 1,
			"widthSegments": 1,
			"heightSegments": 1,
			"depthSegments": 1
		},
		{
			"uuid": "0c5e3dc5-116d-49ee-9832-dd6720a15819",
			"type": "CylinderGeometry",
			"radiusTop": 1,
			"radiusBottom": 1,
			"height": 1,
			"radialSegments": 32,
			"heightSegments": 1,
			"openEnded": false,
			"thetaStart": 0,
			"thetaLength": 6.283185307179586
		},
		{
			"uuid": "9794782d-5a5e-4f28-88cb-6f81e3897658",
			"type": "CylinderGeometry",
			"radiusTop": 1,
			"radiusBottom": 1,
			"height": 1,
			"radialSegments": 32,
			"heightSegments": 1,
			"openEnded": false,
			"thetaStart": 0,
			"thetaLength": 6.283185307179586
		},
		{
			"uuid": "3d6e13bc-7111-424d-a3ae-e2e30b17ea2b",
			"type": "BoxGeometry",
			"width": 1,
			"height": 1,
			"depth": 1,
			"widthSegments": 1,
			"heightSegments": 1,
			"depthSegments": 1
		},
		{
			"uuid": "04be57e0-ceac-4000-af80-d3d8d37820b2",
			"type": "CylinderGeometry",
			"radiusTop": 1,
			"radiusBottom": 1,
			"height": 1,
			"radialSegments": 32,
			"heightSegments": 1,
			"openEnded": false,
			"thetaStart": 0,
			"thetaLength": 6.283185307179586
		},
		{
			"uuid": "d2315d33-765f-4404-a7a8-9c44452c4b62",
			"type": "BoxGeometry",
			"name": "base garra",
			"width": 1,
			"height": 1,
			"depth": 1,
			"widthSegments": 1,
			"heightSegments": 1,
			"depthSegments": 1
		},
		{
			"uuid": "781ced4e-49d5-488e-a150-6df1a747abab",
			"type": "BoxGeometry",
			"width": 1,
			"height": 1,
			"depth": 1,
			"widthSegments": 1,
			"heightSegments": 1,
			"depthSegments": 1
		},
		{
			"uuid": "90b7870d-7014-43ee-9977-540f4bc803c7",
			"type": "BoxGeometry",
			"width": 1,
			"height": 1,
			"depth": 1,
			"widthSegments": 1,
			"heightSegments": 1,
			"depthSegments": 1
		},
		{
			"uuid": "384b8098-17d3-4879-88ad-5e25656baaef",
			"type": "BoxGeometry",
			"width": 1,
			"height": 1,
			"depth": 1,
			"widthSegments": 1,
			"heightSegments": 1,
			"depthSegments": 1
		},
		{
			"uuid": "e1ecb6f0-a382-46bf-83e5-ac8dc462c550",
			"type": "BoxGeometry",
			"name": "raspberry 1",
			"width": 1,
			"height": 1,
			"depth": 1,
			"widthSegments": 1,
			"heightSegments": 1,
			"depthSegments": 1
		},
		{
			"uuid": "6c9f86b0-ae65-494e-a704-91659866f567",
			"type": "BoxGeometry",
			"name": "pantalla",
			"width": 1,
			"height": 1,
			"depth": 1,
			"widthSegments": 1,
			"heightSegments": 1,
			"depthSegments": 1
		},
		{
			"uuid": "01faaee5-f9ae-448e-8903-1acea5a65d12",
			"type": "BoxGeometry",
			"width": 1,
			"height": 1,
			"depth": 1,
			"widthSegments": 1,
			"heightSegments": 1,
			"depthSegments": 1
		},
		{
			"uuid": "ea3e6061-da4c-46d5-8573-90366029d753",
			"type": "CylinderGeometry",
			"radiusTop": 1,
			"radiusBottom": 1,
			"height": 1,
			"radialSegments": 32,
			"heightSegments": 1,
			"openEnded": false,
			"thetaStart": 0,
			"thetaLength": 6.283185307179586
		},
		{
			"uuid": "dbab9269-a022-443a-915b-c79aae863af7",
			"type": "BoxGeometry",
			"width": 1,
			"height": 1,
			"depth": 1,
			"widthSegments": 1,
			"heightSegments": 1,
			"depthSegments": 1
		},
		{
			"uuid": "8fba4ac6-74b0-413a-ab37-0f6a81db8d90",
			"type": "BoxGeometry",
			"width": 1,
			"height": 1,
			"depth": 1,
			"widthSegments": 1,
			"heightSegments": 1,
			"depthSegments": 1
		},
		{
			"uuid": "91e26e6a-e08e-4289-9d03-2d2c96cea6ee",
			"type": "BoxGeometry",
			"width": 1,
			"height": 1,
			"depth": 1,
			"widthSegments": 1,
			"heightSegments": 1,
			"depthSegments": 1
		},
		{
			"uuid": "9ccf5c7d-4d8b-43c5-a171-ee082a0207d8",
			"type": "BoxGeometry",
			"width": 1,
			"height": 1,
			"depth": 1,
			"widthSegments": 1,
			"heightSegments": 1,
			"depthSegments": 1
		},
		{
			"uuid": "eb780773-966f-4e20-bbe9-accd0a8cc1e8",
			"type": "BoxGeometry",
			"width": 1,
			"height": 1,
			"depth": 1,
			"widthSegments": 1,
			"heightSegments": 1,
			"depthSegments": 1
		},
		{
			"uuid": "a301d2e1-26a0-451e-ae94-99c8b70fb20d",
			"type": "BoxGeometry",
			"width": 1,
			"height": 1,
			"depth": 1,
			"widthSegments": 1,
			"heightSegments": 1,
			"depthSegments": 1
		},
		{
			"uuid": "9c4bc828-3746-4956-829e-a37f1ceb54a7",
			"type": "BoxGeometry",
			"width": 1,
			"height": 1,
			"depth": 1,
			"widthSegments": 1,
			"heightSegments": 1,
			"depthSegments": 1
		},
		{
			"uuid": "24a83dfb-a73b-4158-b884-30ffdf48c8d7",
			"type": "BoxGeometry",
			"name": "parte pantalla",
			"width": 1,
			"height": 1,
			"depth": 1,
			"widthSegments": 1,
			"heightSegments": 1,
			"depthSegments": 1
		},
		{
			"uuid": "8565f5e1-bb4a-40b5-af43-67ecf79e3b22",
			"type": "BoxGeometry",
			"name": "raspberry 2",
			"width": 1,
			"height": 1,
			"depth": 1,
			"widthSegments": 1,
			"heightSegments": 1,
			"depthSegments": 1
		},
	       
		{
			"uuid": "ce742b27-ed64-459f-86af-775ba5f8bb97",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 5734267,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "8e29de99-3a3a-456f-9e75-53795052133e",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 15342106,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "a39c2f5f-de93-4c09-99ed-3bdb3b95c34f",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 0,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "b44ea7ec-6ab2-41ea-9b83-88e8d86f0cee",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 0,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "d7473aec-d09d-4a10-96c1-84773dbb96f8",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 0,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "2e04e6d7-2522-45c7-8b0f-659529addbc6",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 15476700,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "f6090931-6c53-48f5-819c-7ac5516cdc18",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 13129302,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "01361de3-a9bb-4855-85a8-2a94e0f77231",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 12314943,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "9517bf3b-5ed8-452d-98c2-bd5adc414399",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 5164842,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "00d0cb87-aee1-45ef-92a7-4bf615f4ff13",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 2503656,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "45105029-4428-4771-8666-b95b872cd569",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 6094716,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "b4a93ea4-babf-4a60-acd0-0cf27f177b2d",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 6255383,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "33a8e7c0-993c-4cd5-95cc-ee5f512dfe22",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 6255383,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "7f81db77-3237-45c5-98c2-47bec5a75099",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 0,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "2d24dd7d-df48-40bf-8063-02421d0690f2",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 1129807,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "63a04b17-5126-415d-8c38-c52c5ccf70df",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 14647681,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "a6769109-f33b-4458-aad2-9804cd7151ba",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 0,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "c27f7f29-b09b-45d6-ade2-1f91fbbe613a",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 0,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "9ffb4905-165b-4061-bc00-835aaff77ce3",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 16774645,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "16cde256-7c38-4e38-8efb-c4a934bc388b",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 1213456,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "6276e133-4e2c-4f73-b201-fd990231086b",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 3394,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "53441df6-ace7-4932-a2f0-c4f5faa31b3a",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 5461958,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "3e858bfa-0d71-462f-b059-556dd82d4aae",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 0,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "4750154e-1eaf-4636-860b-10fb99516001",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 0,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "b9ef2326-99c1-447b-8bf1-81bb092dcc44",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 12382284,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "53a7406b-c52e-43e6-9afb-9600abf17c30",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 12382284,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "1e4e37df-5ecb-4ba8-a1fd-99e6df7cd021",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 265170,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "74c3a09f-07de-4573-914e-8ee5dfc8f9e6",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 265170,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "af31b612-3c48-4401-9bd0-575e18d87b53",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 0,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "47dce5fc-46af-48f8-a581-ddd77f87d9ef",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 0,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "fa7771d5-f7c7-4cfe-9995-64c7e6623a4a",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 0,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
		{
			"uuid": "829c348f-d46e-42c7-9400-e702ad34c993",
			"type": "MeshStandardMaterial",
			"color": 16777215,
			"roughness": 1,
			"metalness": 0,
			"emissive": 1146639,
			"envMapRotation": [0,0,0,
				"XYZ"],
			"envMapIntensity": 1,
			"blendColor": 0
		},
			{
				"uuid": "a31a4756-9b2f-4685-92da-d6dab2e5f886",
				"type": "Group",
				"name": "Group",
				"layers": 1,
				"matrix": [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0.5,1],
				"up": [0,1,0]
			},
			{
				"uuid": "f8234192-7857-4923-a582-57c31db1496e",
				"type": "Group",
				"name": "caja base",
				"layers": 1,
				"matrix": [1,0,0,0,0,1,0,0,0,0,1,0,0,2,0.01,1],
				"up": [0,1,0],
				"children": [
					{
						"uuid": "f374f7b6-34d0-483b-bd79-1833b6a25a53",
						"type": "Mesh",
						"name": "Box",
						"layers": 1,
						"matrix": [6.661338147750939e-16,2.9544232590366235,-0.5209445330007912,0,1.6653345369377347e-17,0.026047226650039577,0.1477211629518312,0,0.14999999999999997,-1.6653345369377347e-17,0,0,0.22941344104313022,2.295347643374007,-0.43639829412099684,1],
						"up": [0,1,0],
						"geometry": "3bff4024-39ab-4875-bce1-bc8f6978f1cf",
						"material": "ce742b27-ed64-459f-86af-775ba5f8bb97"
					},
					{
						"uuid": "31ddb0df-6e4a-4bd6-baf5-90b48610d921",
						"type": "Mesh",
						"name": "Box",
						"layers": 1,
						"matrix": [1.32,0,0,0,0,1,0,0,0,0,0.3,0,-0.361683609204757,0.4855811543455727,-0.9776969033442565,1],
						"up": [0,1,0],
						"geometry": "6d8cd110-50fa-4e85-80be-9eb5b51324eb",
						"material": "8e29de99-3a3a-456f-9e75-53795052133e"
					},
					{
						"uuid": "c2585bf5-a271-486b-882d-ab1ade2ef11e",
						"type": "Mesh",
						"name": "Box",
						"layers": 1,
						"matrix": [1.5,0,0,0,0,1,0,0,0,0,0.3,0,-0.4005721528519232,0.5005571578594883,1.8758050599718186,1],
						"up": [0,1,0],
						"geometry": "6221cd24-23de-4114-8ee3-ccb7333452b9",
						"material": "a39c2f5f-de93-4c09-99ed-3bdb3b95c34f"
					},
					{
						"uuid": "d49eba6c-6fde-4fb5-b791-e645cd30be97",
						"type": "Mesh",
						"name": "Box",
						"layers": 1,
						"matrix": [7.105427357601002e-16,0,-3.2,0,0,1,0,0,0.3,0,6.661338147750939e-17,0,0.460992680889598,0.49722980018215396,0.46425592146605854,1],
						"up": [0,1,0],
						"geometry": "3432b7b7-8234-4398-95a7-19855cd40a33",
						"material": "b44ea7ec-6ab2-41ea-9b83-88e8d86f0cee"
					},
					{
						"uuid": "40bc97af-b1bb-4f8e-b473-11dba1c28605",
						"type": "Mesh",
						"name": "Box",
						"layers": 1,
						"matrix": [0.006044442208570544,0.013799820285452652,-3.1999645356907442,0,0.0027423017247798034,0.9999869189046487,0.004317615179444231,0,0.2999983367777878,-0.0008251280475834309,0.0005631112377820768,0,-1.16728204598011,0.48682230774187907,0.4423093301106725,1],
						"up": [0,1,0],
						"geometry": "8e0b0115-5e99-482d-99d6-1a145b8c4c14",
						"material": "d7473aec-d09d-4a10-96c1-84773dbb96f8"
					},
					{
						"uuid": "17c5e4df-9cbd-48d7-a599-4dbba274d23d",
						"type": "Mesh",
						"name": "Box",
						"layers": 1,
						"matrix": [1.4,0,0,0,0,5.551115123125783e-16,2.5,0,0,-0.3,6.661338147750939e-17,0,-0.40862596557042397,0.13192418506349135,0.48483199165404034,1],
						"up": [0,1,0],
						"geometry": "57054775-f8c6-490c-b475-a2c399a1a303",
						"material": "2e04e6d7-2522-45c7-8b0f-659529addbc6"
					},
					{
						"uuid": "29adb648-6ae3-4ce5-b9d6-e9905442c15f",
						"type": "Mesh",
						"name": "Box",
						"layers": 1,
						"matrix": [6.661338147750939e-16,2.9544232590366235,-0.5209445330007912,0,1.6653345369377347e-17,0.026047226650039577,0.1477211629518312,0,0.14999999999999997,-1.6653345369377347e-17,0,0,-0.9418803137757191,2.1558333540102765,-0.6777793685838984,1],
						"up": [0,1,0],
						"geometry": "d502afed-85ea-4892-851a-d1b8b164f372",
						"material": "f6090931-6c53-48f5-819c-7ac5516cdc18"
					},
					{
						"uuid": "9028d6ed-0313-455d-ae71-c12714dc0670",
						"type": "Mesh",
						"name": "Box",
						"layers": 1,
						"matrix": [1.05,0,0,0,0,2.954423259036624,0.520944533000791,0,0,-0.0520944533000791,0.2954423259036624,0,-0.333412222072613,2.0067301991736137,1.1763395564363648,1],
						"up": [0,1,0],
						"geometry": "a1d4d830-465b-4bc0-a1d6-008043ac3f62",
						"material": "01361de3-a9bb-4855-85a8-2a94e0f77231"
					}]
			},
			{
				"uuid": "458b2061-a5c2-4bab-89fa-19ef89b4aa00",
				"type": "Mesh",
				"name": "Box",
				"layers": 1,
				"matrix": [0.3140157374576644,1.5507860555781199,-5.787612351086876,0,4.163336342344337e-18,0.14488887394336025,0.038822856765378104,0,0.14979443021318603,-0.00203183133289891,0.007582897766789154,0,0.2605243305854552,4.686885089132606,1.7821604726381763,1],
				"up": [0,1,0],
				"geometry": "79f5214f-98fa-4747-8033-74c86d9b7939",
				"material": "9517bf3b-5ed8-452d-98c2-bd5adc414399"
			},
			{
				"uuid": "03b19367-4c28-4852-8521-5bb743dd8e44",
				"type": "Mesh",
				"name": "Box",
				"layers": 1,
				"matrix": [3,0,0,0,0,1.7763568394002505e-15,8,0,0,-0.3,6.661338147750939e-17,0,-0.3651107358407901,1.8221887746966061,-1.3193337808195766,1],
				"up": [0,1,0],
				"geometry": "cefd6bb0-37b6-45dc-aaf0-9d79b5eae7fe",
				"material": "00d0cb87-aee1-45ef-92a7-4bf615f4ff13"
			},
			{
				"uuid": "d3586c58-67bd-4f85-b879-5c618b46b6a2",
				"type": "Mesh",
				"name": "Box",
				"layers": 1,
				"matrix": [-0.3140157374576624,1.5507860555781199,-5.787612351086877,0,-4.163336342344337e-18,0.14488887394336025,0.03882285676537811,0,0.14979443021318606,0.0020318313328989033,-0.007582897766789087,0,-0.9620433952408916,4.566724508195738,1.6591805752378368,1],
				"up": [0,1,0],
				"geometry": "e251a61e-58fc-4b32-bb4a-0c7173ee877a",
				"material": "45105029-4428-4771-8666-b95b872cd569"
			},
			{
				"uuid": "3a775d42-eaa6-4d1a-a24c-be49f71ec828",
				"type": "Mesh",
				"name": "Cylinder",
				"layers": 1,
				"matrix": [2.220446049250313e-16,2.220446049250313e-16,1,0,-1,0,2.220446049250313e-16,0,0,-1,2.220446049250313e-16,0,1.6818747102495268,1.0451981392335603,-3.5186952452738565,1],
				"up": [0,1,0],
				"geometry": "0c5e3dc5-116d-49ee-9832-dd6720a15819",
				"material": "b4a93ea4-babf-4a60-acd0-0cf27f177b2d"
			},
			{
				"uuid": "118121f4-71f5-496e-a2b6-a7eb99d39f48",
				"type": "Mesh",
				"name": "Cylinder",
				"layers": 1,
				"matrix": [2.220446049250313e-16,2.220446049250313e-16,1,0,-1,0,2.220446049250313e-16,0,0,-1,2.220446049250313e-16,0,-2.3937069673651132,0.9935726223117225,-3.4806217939657706,1],
				"up": [0,1,0],
				"geometry": "9794782d-5a5e-4f28-88cb-6f81e3897658",
				"material": "33a8e7c0-993c-4cd5-95cc-ee5f512dfe22"
			},
			{
				"uuid": "dcfc5b49-f17e-4d97-a42a-86cc58844877",
				"type": "Mesh",
				"name": "Box",
				"visible": false,
				"layers": 1,
				"matrix": [1,0,0,0,0,0.5,0,0,0,0,1,0,-0.37555113002590557,1.4361515895478554,2.1926904525792947,1],
				"up": [0,1,0],
				"geometry": "3d6e13bc-7111-424d-a3ae-e2e30b17ea2b",
				"material": "7f81db77-3237-45c5-98c2-47bec5a75099"
			},
			{
				"uuid": "7f1ad3f0-cfaa-4c6a-99fd-765660f5728c",
				"type": "Mesh",
				"name": "Cylinder",
				"layers": 1,
				"matrix": [0.6,0,0,0,0,1.3322676295501878e-16,0.6,0,0,-0.6,1.3322676295501878e-16,0,-0.3680158770978337,0.639457512032757,1.856431437379648,1],
				"up": [0,1,0],
				"geometry": "04be57e0-ceac-4000-af80-d3d8d37820b2",
				"material": "2d24dd7d-df48-40bf-8063-02421d0690f2"
			},
			{
				"uuid": "28fa19e7-1915-43b4-b4d8-066960770d6d",
				"type": "Mesh",
				"name": "Box",
				"layers": 1,
				"matrix": [0.7,0,0,0,0,0.5,0,0,0,0,1,0,-0.3414636301061616,3.8591149321738283,4.805824548410337,1],
				"up": [0,1,0],
				"geometry": "d2315d33-765f-4404-a7a8-9c44452c4b62",
				"material": "63a04b17-5126-415d-8c38-c52c5ccf70df",
				"children": [
					{
						"uuid": "9598edf5-fe81-41b0-b754-9c1ee9301cdb",
						"type": "Mesh",
						"name": "Box",
						"layers": 1,
						"matrix": [0.8387893552061201,2.498001805406602e-16,1.2435563588325627,0,-0.4145187862775209,0,0.2795964517353734,0,-2.7755575615628914e-17,-0.5,5.551115123125783e-17,0,1.0547759651754784,0.2068283689111956,0.7179642050817465,1],
						"up": [0,1,0],
						"geometry": "781ced4e-49d5-488e-a150-6df1a747abab",
						"material": "a6769109-f33b-4458-aad2-9804cd7151ba"
					},
					{
						"uuid": "aaccf8fe-07a0-46c7-bb87-a087865cfd03",
						"type": "Mesh",
						"name": "Box",
						"layers": 1,
						"matrix": [-0.75,2.498001805406602e-16,1.2990381056766582,0,-0.4330127018922194,-1.1102230246251565e-16,-0.24999999999999997,0,0,-0.5,0,0,-0.9201633247141274,0.1272987355898203,0.5631943523810525,1],
						"up": [0,1,0],
						"geometry": "90b7870d-7014-43ee-9977-540f4bc803c7",
						"material": "c27f7f29-b09b-45d6-ade2-1f91fbbe613a"
					}]
			},
			{
				"uuid": "e05458c9-256e-4838-9be2-c29f72677d1e",
				"type": "Mesh",
				"name": "Box",
				"layers": 1,
				"matrix": [3,0,0,0,0,1.7763568394002505e-15,8,0,0,-0.3,6.661338147750939e-17,0,-0.28807029560611097,2.143727031956033,-5.232787515405793,1],
				"up": [0,1,0],
				"geometry": "384b8098-17d3-4879-88ad-5e25656baaef",
				"material": "9ffb4905-165b-4061-bc00-835aaff77ce3"
			},
			{
				"uuid": "20b6a032-a822-4ced-a234-f58ed7491688",
				"type": "Mesh",
				"name": "Box",
				"layers": 1,
				"matrix": [1,0,0,0,0,4.440892098500626e-16,2,0,0,-0.3,6.661338147750939e-17,0,0.01417294299720151,2.449224664755656,-7.645706586438138,1],
				"up": [0,1,0],
				"geometry": "e1ecb6f0-a382-46bf-83e5-ac8dc462c550",
				"material": "16cde256-7c38-4e38-8efb-c4a934bc388b"
			},
			{
				"uuid": "c8e9c116-1cd8-4a73-ad45-a6f22f130816",
				"type": "Mesh",
				"name": "Box",
				"layers": 1,
				"matrix": [1.5,0,0,0,0,3.3306690738754696e-16,1.5,0,0,-0.3,6.661338147750939e-17,0,0.22056579485416172,2.5769871693795054,-5.1511666707843595,1],
				"up": [0,1,0],
				"geometry": "6c9f86b0-ae65-494e-a704-91659866f567",
				"material": "6276e133-4e2c-4f73-b201-fd990231086b"
			},
			{
				"uuid": "2ff886d7-8ae5-4b28-b099-4407e822c45b",
				"type": "Mesh",
				"name": "Box",
				"layers": 1,
				"matrix": [1.5,0,0,0,0,1.5,0,0,0,0,0.7,0,-0.34127899985944854,2.2820842947205833,3.0112806238710483,1],
				"up": [0,1,0],
				"geometry": "01faaee5-f9ae-448e-8903-1acea5a65d12",
				"material": "53441df6-ace7-4932-a2f0-c4f5faa31b3a"
			},
			{
				"uuid": "c8f082a7-b631-40d2-8652-e016408bab64",
				"type": "Mesh",
				"name": "Cylinder",
				"layers": 1,
				"matrix": [0.6,0,0,0,0,1.3322676295501878e-16,0.6,0,0,-0.6,1.3322676295501878e-16,0,-0.38539889164223307,2.244648443217466,3.5964126822955444,1],
				"up": [0,1,0],
				"geometry": "ea3e6061-da4c-46d5-8573-90366029d753",
				"material": "3e858bfa-0d71-462f-b059-556dd82d4aae"
			},
			{
				"uuid": "52df5c53-e6a7-43a1-a9ff-bf473f040dc6",
				"type": "Mesh",
				"name": "Box",
				"layers": 1,
				"matrix": [1.2,0,0,0,0,0.5,0,0,0,0,1.2,0,-0.3455182568821378,1.463735726384027,1.9909446529594117,1],
				"up": [0,1,0],
				"geometry": "dbab9269-a022-443a-915b-c79aae863af7",
				"material": "4750154e-1eaf-4636-860b-10fb99516001"
			},
			{
				"uuid": "0cb693f9-317e-4fa4-9bdd-0ab00d4f4793",
				"type": "Mesh",
				"name": "Box",
				"layers": 1,
				"matrix": [1,0,0,0,0,6.661338147750939e-16,3,0,0,-1,2.220446049250313e-16,0,0.6425582079029493,1.0186503402127693,-2.8780517432912047,1],
				"up": [0,1,0],
				"geometry": "8fba4ac6-74b0-413a-ab37-0f6a81db8d90",
				"material": "b9ef2326-99c1-447b-8bf1-81bb092dcc44"
			},
			{
				"uuid": "0c5cd936-3123-4c9f-8a40-9cac58727d1f",
				"type": "Mesh",
				"name": "Box",
				"layers": 1,
				"matrix": [1,0,0,0,0,6.661338147750939e-16,3,0,0,-1,2.220446049250313e-16,0,-1.3009819335777406,1.1035872857536662,-2.8014381092615297,1],
				"up": [0,1,0],
				"geometry": "91e26e6a-e08e-4289-9d03-2d2c96cea6ee",
				"material": "53a7406b-c52e-43e6-9afb-9600abf17c30"
			},
			{
				"uuid": "9cd73c09-44b0-450a-b9ab-949e17d22898",
				"type": "Mesh",
				"name": "Box",
				"layers": 1,
				"matrix": [0.7,0,0,0,0,0.7,0,0,0,0,1,0,-1.1285686354342301,2.479188241404671,0.317641586404227,1],
				"up": [0,1,0],
				"geometry": "9ccf5c7d-4d8b-43c5-a171-ee082a0207d8",
				"material": "1e4e37df-5ecb-4ba8-a1fd-99e6df7cd021"
			},
			{
				"uuid": "f714487f-2a0e-453a-9b82-dfdf121a02ec",
				"type": "Mesh",
				"name": "Box",
				"layers": 1,
				"matrix": [0.7,0,0,0,0,0.7,0,0,0,0,1,0,0.4138750432237144,2.467147808420551,0.29331886735441715,1],
				"up": [0,1,0],
				"geometry": "eb780773-966f-4e20-bbe9-accd0a8cc1e8",
				"material": "74c3a09f-07de-4573-914e-8ee5dfc8f9e6"
			},
			{
				"uuid": "813a3b4c-b95b-40c2-9be6-8883492a2865",
				"type": "Mesh",
				"name": "Box",
				"layers": 1,
				"matrix": [1,0,0,0,0,0.3,0,0,0,0,0.3,0,1.056569841062026,0.36138281615256607,-3.1559783163743322,1],
				"up": [0,1,0],
				"geometry": "a301d2e1-26a0-451e-ae94-99c8b70fb20d",
				"material": "af31b612-3c48-4401-9bd0-575e18d87b53"
			},
			{
				"uuid": "50e36c90-294b-4aea-8933-429e0650ec77",
				"type": "Mesh",
				"name": "Box",
				"layers": 1,
				"matrix": [1,0,0,0,0,0.3,0,0,0,0,0.3,0,-1.7856584286087291,0.4109790793240313,-3.1657560757622547,1],
				"up": [0,1,0],
				"geometry": "9c4bc828-3746-4956-829e-a37f1ceb54a7",
				"material": "47dce5fc-46af-48f8-a581-ddd77f87d9ef"
			},
			{
				"uuid": "1781e406-a96e-4d18-b5ad-9cc5a2afc20c",
				"type": "Mesh",
				"name": "Box",
				"layers": 1,
				"matrix": [1,0,0,0,0,2.6645352591003756e-16,1.2,0,0,-0.1,2.2204460492503132e-17,0,0.20592790387750015,2.7318035786421957,-5.117617577205671,1],
				"up": [0,1,0],
				"geometry": "24a83dfb-a73b-4158-b884-30ffdf48c8d7",
				"material": "fa7771d5-f7c7-4cfe-9995-64c7e6623a4a"
			},
			{
				"uuid": "6596c4a3-3243-40a9-b158-9852bb9ec4a6",
				"type": "Mesh",
				"name": "Box",
				"layers": 1,
				"matrix": [1,0,0,0,0,4.440892098500626e-16,2,0,0,-0.3,6.661338147750939e-17,0,-0.30821912081059377,2.5633651933126345,-2.510256688041548,1],
				"up": [0,1,0],
				"geometry": "8565f5e1-bb4a-40b5-af43-67ecf79e3b22",
				"material": "829c348f-d46e-42c7-9400-e702ad34c993"
            }
        ];

    // Recorre las geometrías adicionales y las agrega a la escena
    additionalGeometries.forEach(geometryData => {
      let geometry;

      switch (geometryData.type) {
        case 'BoxGeometry':
          geometry = new THREE.BoxGeometry(
            geometryData.width,
            geometryData.height,
            geometryData.depth,
            geometryData.widthSegments,
            geometryData.heightSegments,
            geometryData.depthSegments
          );
          break;
        case 'CylinderGeometry':
          geometry = new THREE.CylinderGeometry(
            geometryData.radiusTop,
            geometryData.radiusBottom,
            geometryData.height,
            geometryData.radialSegments,
            geometryData.heightSegments,
            geometryData.openEnded,
            geometryData.thetaStart,
            geometryData.thetaLength
          );
          break;
        // Agrega más casos según sea necesario para otros tipos de geometrías
        default:
          console.error('Unknown geometry type:', geometryData.type);
          return;
      }

      const material = new THREE.MeshBasicMaterial({ color: 0xff0000 });
      const mesh = new THREE.Mesh(geometry, material);
      mesh.name = geometryData.name;
      scene.add(mesh);
    });

    // Crea una cámara, un renderizador y renderiza la escena
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);
    
    // Posiciona la cámara
    camera.position.z = 5;

    // Función de animación
    function animate() {
      requestAnimationFrame(animate);
      renderer.render(scene, camera);
    }
    animate();
  })
  .catch(error => {
    console.error('There has been a problem with your fetch operation:', error);
  });
