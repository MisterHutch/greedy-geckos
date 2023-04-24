  // TODO: Add SDKs for Firebase products that you want to use
        // Your web app's Firebase configuration
        // For Firebase JS SDK v7.20.0 and later, measurementId is optional
        const firebaseConfig = {
            apiKey: "AIzaSyCbBCIX-o8UeXEtgaPGQ_Xzuoo3cc6Vc9U",
            authDomain: "greedygeckoz-14438.firebaseapp.com",
            databaseURL: "https://greedygeckoz-14438-default-rtdb.firebaseio.com",
            projectId: "greedygeckoz-14438",
            storageBucket: "greedygeckoz-14438.appspot.com",
            messagingSenderId: "465420491168",
            appId: "1:465420491168:web:a55f02e61c0be494e06cc5",
            measurementId: "G-1T330PGK88"
        };

        firebase.initializeApp(firebaseConfig);
        
        let database = firebase.database();
        
        function save(ip, city, country, time, date) {
            database.ref('country/' + country).set({
                ip: ip,
                city: city,
                country: country,
                time: time,
                date: date

            })
        }


