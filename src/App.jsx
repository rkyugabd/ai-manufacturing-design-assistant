import { useState } from "react";
import "./App.css";


function App() {

  const [category, setCategory] = useState("Trailer Design");
  const [projectName, setProjectName] = useState("");
  const [requirements, setRequirements] = useState("");

  const [report, setReport] = useState("");
  const [pdfUrl, setPdfUrl] = useState("");

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");



  const generateReport = async () => {

    setLoading(true);
    setError("");
    setReport("");
    setPdfUrl("");


    try {

      const response = await fetch(
         "https://ai-manufacturing-design-assistant.onrender.com/generate-report",
        {
          method: "POST",

          headers: {
            "Content-Type": "application/json",
          },

          body: JSON.stringify({

            category: category,

            projectName: projectName,

            requirements: requirements

          })

        }
      );



      if (!response.ok) {

        throw new Error(
          "Backend returned error: " + response.status
        );

      }



      const data = await response.json();



      setReport(
        data.report
      );


      setPdfUrl(
        data.pdf_url
      );



    } catch (err) {


      console.error(err);


      setError(
        "Error: " + err.message
      );


    } finally {

      setLoading(false);

    }

  };





  return (

    <div className="page">


      <div className="container">


        <h1>
          AI Manufacturing Design Assistant
        </h1>


        <p className="subtitle">
          Generate manufacturing engineering proposals with AI
        </p>



        <div className="card">


          <label>
            Manufacturing Category
          </label>


          <select

            value={category}

            onChange={
              (e) => setCategory(e.target.value)
            }

          >

            <option>
              Trailer Design
            </option>

            <option>
              Gearbox Design
            </option>

            <option>
              Sheet Metal Design
            </option>

            <option>
              Machine Parts
            </option>

            <option>
              Jigs & Fixtures
            </option>


          </select>




          <label>
            Project Name
          </label>


          <input

            type="text"

            placeholder="Example: 50 Ton Grain Trailer"

            value={projectName}

            onChange={
              (e)=>setProjectName(e.target.value)
            }

          />





          <label>
            Requirements
          </label>


          <textarea

            placeholder="
Example:

Payload: 50 tons
Material: Steel
Region: Ontario
Axle: 3 axle
Hydraulic discharge
Lifetime: 10 years
            "

            value={requirements}

            onChange={
              (e)=>setRequirements(e.target.value)
            }

          />





          <button

            onClick={generateReport}

            disabled={loading}

          >

            {
              loading
              ?
              "Generating..."
              :
              "Generate Project Report"
            }


          </button>



        </div>





        {
          error &&

          <div className="error">

            {error}

          </div>

        }





        {
          report &&

          <div className="card report">


            <h2>
              Engineering Project Report
            </h2>


            <pre>
              {report}
            </pre>



            {

              pdfUrl &&

              <div className="pdf-buttons">


                <a

                  href={pdfUrl}

                  target="_blank"

                  rel="noreferrer"

                >

                  View PDF

                </a>



                <a

                  href={pdfUrl}

                  download

                >

                  Download PDF

                </a>



              </div>

            }


          </div>

        }



      </div>


    </div>

  );

}


export default App;