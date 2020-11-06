<?python
title="Calculating LP Performance"
?>

<html xmlns="http://www.w3.org/xhtml"
      xmlns:py="http://purl.org/kid/ns#"
>
<head>
  <meta content="text/html; charset=ISO-8859-1"
 http-equiv="content-type" />
  <title py:content="title" />
</head>
<body>
<form action="resultPage" method="POST">
  <table style="text-align: left; width: 437px;" border="1"
 cellpadding="2" cellspacing="2">
    <tbody>
      <tr>
        <td style="width: 202px;">Flowrate, BPH   </td>
        <td style="width: 218px;"><input type="text" name="FlowRate" />
        </td>
      </tr>
      <tr>
        <td style="width: 202px;">Expected Flowrate, BPH   </td>
        <td style="width: 218px;"><input type="text" name="Expected" />
        </td>
      </tr>
      <tr>
        <td style="width: 202px;">Product
(crude, refined product, water)
        </td>
        <td style="width: 218px;">
        <select name="Product">
        <option>Crude Oil</option>
        <option>Refined Product</option>
        <option>Water</option>
        </select>
        </td>
      </tr>
      <tr>
        <td style="width: 202px;">Fluid
density, lb/ft3
        </td>
        <td style="width: 218px;"><input type="text" name="Density" />
        </td>
      </tr>
      <tr>
        <td style="width: 202px;">Viscosity, cP
        </td>
        <td style="width: 218px;"><input type="text" name="Viscosity" />
        </td>
      </tr>
      <tr>
        <td style="width: 202px;">Pipe
ID, inches
        </td>
        <td style="width: 218px;"><input type="text" name="ID" />
        </td>
      </tr>
      <tr>
        <td style="width: 202px;">Length, miles
        </td>
        <td style="width: 218px;"><input type="text" name="Length" />
        </td>
      </tr>
      <tr>
        <td style="width: 202px;"><input type="submit"/>
        </td>
        <td style="width: 218px;"><input type="reset"/>
        </td>
      </tr>
    </tbody>
  </table>
</form>
</body>
</html>
