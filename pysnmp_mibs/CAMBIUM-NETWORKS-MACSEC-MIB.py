_G='MacSecViolationMode'
_F='cnMacSecPortIndex'
_E='CAMBIUM-NETWORKS-MACSEC-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
cnMacSecMib=ModuleIdentity((1,3,6,1,4,1,17713,24,10))
if mibBuilder.loadTexts:cnMacSecMib.setRevisions(('2021-11-28 00:00','2021-06-04 00:00'))
class MacSecViolationMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('protect',1),('restrict',2),('shutdown',3)))
_CnMacSecPort_ObjectIdentity=ObjectIdentity
cnMacSecPort=_CnMacSecPort_ObjectIdentity((1,3,6,1,4,1,17713,24,10,1))
_CnMacSecPortTable_Object=MibTable
cnMacSecPortTable=_CnMacSecPortTable_Object((1,3,6,1,4,1,17713,24,10,1,1))
if mibBuilder.loadTexts:cnMacSecPortTable.setStatus(_A)
_CnMacSecPortEntry_Object=MibTableRow
cnMacSecPortEntry=_CnMacSecPortEntry_Object((1,3,6,1,4,1,17713,24,10,1,1,1))
cnMacSecPortEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:cnMacSecPortEntry.setStatus(_A)
class _CnMacSecPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,52))
_CnMacSecPortIndex_Type.__name__=_C
_CnMacSecPortIndex_Object=MibTableColumn
cnMacSecPortIndex=_CnMacSecPortIndex_Object((1,3,6,1,4,1,17713,24,10,1,1,1,1),_CnMacSecPortIndex_Type())
cnMacSecPortIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cnMacSecPortIndex.setStatus(_A)
class _CnMacSecPortStatus_Type(Integer32):defaultValue=0
_CnMacSecPortStatus_Type.__name__=_C
_CnMacSecPortStatus_Object=MibTableColumn
cnMacSecPortStatus=_CnMacSecPortStatus_Object((1,3,6,1,4,1,17713,24,10,1,1,1,2),_CnMacSecPortStatus_Type())
cnMacSecPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMacSecPortStatus.setStatus(_A)
class _CnMacSecPortMode_Type(MacSecViolationMode):defaultValue=1
_CnMacSecPortMode_Type.__name__=_G
_CnMacSecPortMode_Object=MibTableColumn
cnMacSecPortMode=_CnMacSecPortMode_Object((1,3,6,1,4,1,17713,24,10,1,1,1,3),_CnMacSecPortMode_Type())
cnMacSecPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMacSecPortMode.setStatus(_A)
class _CnMacSecPortMaxAddr_Type(Integer32):defaultValue=1
_CnMacSecPortMaxAddr_Type.__name__=_C
_CnMacSecPortMaxAddr_Object=MibTableColumn
cnMacSecPortMaxAddr=_CnMacSecPortMaxAddr_Object((1,3,6,1,4,1,17713,24,10,1,1,1,4),_CnMacSecPortMaxAddr_Type())
cnMacSecPortMaxAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMacSecPortMaxAddr.setStatus(_A)
_CnMacSecPortNumAddr_Type=Integer32
_CnMacSecPortNumAddr_Object=MibTableColumn
cnMacSecPortNumAddr=_CnMacSecPortNumAddr_Object((1,3,6,1,4,1,17713,24,10,1,1,1,5),_CnMacSecPortNumAddr_Type())
cnMacSecPortNumAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cnMacSecPortNumAddr.setStatus(_A)
_CnMacSecPortNumViolations_Type=Gauge32
_CnMacSecPortNumViolations_Object=MibTableColumn
cnMacSecPortNumViolations=_CnMacSecPortNumViolations_Object((1,3,6,1,4,1,17713,24,10,1,1,1,6),_CnMacSecPortNumViolations_Type())
cnMacSecPortNumViolations.setMaxAccess(_D)
if mibBuilder.loadTexts:cnMacSecPortNumViolations.setStatus(_A)
_CnMacSecPortLastViolationAddr_Type=MacAddress
_CnMacSecPortLastViolationAddr_Object=MibTableColumn
cnMacSecPortLastViolationAddr=_CnMacSecPortLastViolationAddr_Object((1,3,6,1,4,1,17713,24,10,1,1,1,7),_CnMacSecPortLastViolationAddr_Type())
cnMacSecPortLastViolationAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cnMacSecPortLastViolationAddr.setStatus(_A)
_CnMacSecPortLastViolationTime_Type=DateAndTime
_CnMacSecPortLastViolationTime_Object=MibTableColumn
cnMacSecPortLastViolationTime=_CnMacSecPortLastViolationTime_Object((1,3,6,1,4,1,17713,24,10,1,1,1,8),_CnMacSecPortLastViolationTime_Type())
cnMacSecPortLastViolationTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cnMacSecPortLastViolationTime.setStatus(_A)
_CnMacSecGlobalDebug_Type=Integer32
_CnMacSecGlobalDebug_Object=MibScalar
cnMacSecGlobalDebug=_CnMacSecGlobalDebug_Object((1,3,6,1,4,1,17713,24,10,2),_CnMacSecGlobalDebug_Type())
cnMacSecGlobalDebug.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMacSecGlobalDebug.setStatus(_A)
_CnMacSecDebugOption_Type=Integer32
_CnMacSecDebugOption_Object=MibScalar
cnMacSecDebugOption=_CnMacSecDebugOption_Object((1,3,6,1,4,1,17713,24,10,3),_CnMacSecDebugOption_Type())
cnMacSecDebugOption.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMacSecDebugOption.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_G:MacSecViolationMode,'cnMacSecMib':cnMacSecMib,'cnMacSecPort':cnMacSecPort,'cnMacSecPortTable':cnMacSecPortTable,'cnMacSecPortEntry':cnMacSecPortEntry,_F:cnMacSecPortIndex,'cnMacSecPortStatus':cnMacSecPortStatus,'cnMacSecPortMode':cnMacSecPortMode,'cnMacSecPortMaxAddr':cnMacSecPortMaxAddr,'cnMacSecPortNumAddr':cnMacSecPortNumAddr,'cnMacSecPortNumViolations':cnMacSecPortNumViolations,'cnMacSecPortLastViolationAddr':cnMacSecPortLastViolationAddr,'cnMacSecPortLastViolationTime':cnMacSecPortLastViolationTime,'cnMacSecGlobalDebug':cnMacSecGlobalDebug,'cnMacSecDebugOption':cnMacSecDebugOption})