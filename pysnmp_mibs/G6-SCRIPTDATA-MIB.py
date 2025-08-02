_H='read-only'
_G='variablesIndex'
_F='read-write'
_E='not-accessible'
_D='parameterIndex'
_C='G6-SCRIPTDATA-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
g6,=mibBuilder.importSymbols('MICROSENS-G6-MIB','g6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
management=ModuleIdentity((1,3,6,1,4,1,3181,10,6,3))
if mibBuilder.loadTexts:management.setRevisions(('2018-02-12 16:19',))
_Scriptdata_ObjectIdentity=ObjectIdentity
scriptdata=_Scriptdata_ObjectIdentity((1,3,6,1,4,1,3181,10,6,3,77))
_ParameterTable_Object=MibTable
parameterTable=_ParameterTable_Object((1,3,6,1,4,1,3181,10,6,3,77,1))
if mibBuilder.loadTexts:parameterTable.setStatus(_A)
_ParameterEntry_Object=MibTableRow
parameterEntry=_ParameterEntry_Object((1,3,6,1,4,1,3181,10,6,3,77,1,1))
parameterEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:parameterEntry.setStatus(_A)
class _ParameterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_ParameterIndex_Type.__name__=_B
_ParameterIndex_Object=MibTableColumn
parameterIndex=_ParameterIndex_Object((1,3,6,1,4,1,3181,10,6,3,77,1,1,1),_ParameterIndex_Type())
parameterIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:parameterIndex.setStatus(_A)
_ParameterName_Type=DisplayString
_ParameterName_Object=MibTableColumn
parameterName=_ParameterName_Object((1,3,6,1,4,1,3181,10,6,3,77,1,1,2),_ParameterName_Type())
parameterName.setMaxAccess(_F)
if mibBuilder.loadTexts:parameterName.setStatus(_A)
_ParameterValue_Type=DisplayString
_ParameterValue_Object=MibTableColumn
parameterValue=_ParameterValue_Object((1,3,6,1,4,1,3181,10,6,3,77,1,1,3),_ParameterValue_Type())
parameterValue.setMaxAccess(_F)
if mibBuilder.loadTexts:parameterValue.setStatus(_A)
_VariablesTable_Object=MibTable
variablesTable=_VariablesTable_Object((1,3,6,1,4,1,3181,10,6,3,77,100))
if mibBuilder.loadTexts:variablesTable.setStatus(_A)
_VariablesEntry_Object=MibTableRow
variablesEntry=_VariablesEntry_Object((1,3,6,1,4,1,3181,10,6,3,77,100,1))
variablesEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:variablesEntry.setStatus(_A)
class _VariablesIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_VariablesIndex_Type.__name__=_B
_VariablesIndex_Object=MibTableColumn
variablesIndex=_VariablesIndex_Object((1,3,6,1,4,1,3181,10,6,3,77,100,1,1),_VariablesIndex_Type())
variablesIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:variablesIndex.setStatus(_A)
_VariablesName_Type=DisplayString
_VariablesName_Object=MibTableColumn
variablesName=_VariablesName_Object((1,3,6,1,4,1,3181,10,6,3,77,100,1,2),_VariablesName_Type())
variablesName.setMaxAccess(_H)
if mibBuilder.loadTexts:variablesName.setStatus(_A)
_VariablesValue_Type=DisplayString
_VariablesValue_Object=MibTableColumn
variablesValue=_VariablesValue_Object((1,3,6,1,4,1,3181,10,6,3,77,100,1,3),_VariablesValue_Type())
variablesValue.setMaxAccess(_H)
if mibBuilder.loadTexts:variablesValue.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'management':management,'scriptdata':scriptdata,'parameterTable':parameterTable,'parameterEntry':parameterEntry,_D:parameterIndex,'parameterName':parameterName,'parameterValue':parameterValue,'variablesTable':variablesTable,'variablesEntry':variablesEntry,_G:variablesIndex,'variablesName':variablesName,'variablesValue':variablesValue})