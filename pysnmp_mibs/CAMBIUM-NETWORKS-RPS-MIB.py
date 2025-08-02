_G='cnRPSStatus'
_F='cnRPSMaximumWatts'
_E='cnRPSIndex'
_D='Integer32'
_C='CAMBIUM-NETWORKS-RPS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
cnRPSMib=ModuleIdentity((1,3,6,1,4,1,17713,24,6))
if mibBuilder.loadTexts:cnRPSMib.setRevisions(('2022-09-08 20:00','2020-07-03 00:00'))
_CnRPSTable_Object=MibTable
cnRPSTable=_CnRPSTable_Object((1,3,6,1,4,1,17713,24,6,1))
if mibBuilder.loadTexts:cnRPSTable.setStatus(_A)
_CnRPSTableEntry_Object=MibTableRow
cnRPSTableEntry=_CnRPSTableEntry_Object((1,3,6,1,4,1,17713,24,6,1,1))
cnRPSTableEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cnRPSTableEntry.setStatus(_A)
class _CnRPSIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_CnRPSIndex_Type.__name__=_D
_CnRPSIndex_Object=MibTableColumn
cnRPSIndex=_CnRPSIndex_Object((1,3,6,1,4,1,17713,24,6,1,1,1),_CnRPSIndex_Type())
cnRPSIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cnRPSIndex.setStatus(_A)
_CnRPSMaximumVoltage_Type=Integer32
_CnRPSMaximumVoltage_Object=MibTableColumn
cnRPSMaximumVoltage=_CnRPSMaximumVoltage_Object((1,3,6,1,4,1,17713,24,6,1,1,2),_CnRPSMaximumVoltage_Type())
cnRPSMaximumVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:cnRPSMaximumVoltage.setStatus(_A)
if mibBuilder.loadTexts:cnRPSMaximumVoltage.setUnits('volts')
_CnRPSMaximumCurrent_Type=Integer32
_CnRPSMaximumCurrent_Object=MibTableColumn
cnRPSMaximumCurrent=_CnRPSMaximumCurrent_Object((1,3,6,1,4,1,17713,24,6,1,1,3),_CnRPSMaximumCurrent_Type())
cnRPSMaximumCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:cnRPSMaximumCurrent.setStatus(_A)
if mibBuilder.loadTexts:cnRPSMaximumCurrent.setUnits('amps')
_CnRPSMaximumWatts_Type=Integer32
_CnRPSMaximumWatts_Object=MibTableColumn
cnRPSMaximumWatts=_CnRPSMaximumWatts_Object((1,3,6,1,4,1,17713,24,6,1,1,4),_CnRPSMaximumWatts_Type())
cnRPSMaximumWatts.setMaxAccess(_B)
if mibBuilder.loadTexts:cnRPSMaximumWatts.setStatus(_A)
if mibBuilder.loadTexts:cnRPSMaximumWatts.setUnits('watts')
class _CnRPSStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ok',1),('error',2),('notpresent',3)))
_CnRPSStatus_Type.__name__=_D
_CnRPSStatus_Object=MibTableColumn
cnRPSStatus=_CnRPSStatus_Object((1,3,6,1,4,1,17713,24,6,1,1,5),_CnRPSStatus_Type())
cnRPSStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cnRPSStatus.setStatus(_A)
_CnRPSCurrentInputVoltage_Type=Integer32
_CnRPSCurrentInputVoltage_Object=MibTableColumn
cnRPSCurrentInputVoltage=_CnRPSCurrentInputVoltage_Object((1,3,6,1,4,1,17713,24,6,1,1,6),_CnRPSCurrentInputVoltage_Type())
cnRPSCurrentInputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:cnRPSCurrentInputVoltage.setStatus(_A)
if mibBuilder.loadTexts:cnRPSCurrentInputVoltage.setUnits('volts')
cnRPSTrapMsg=NotificationType((1,3,6,1,4,1,17713,24,6,2))
cnRPSTrapMsg.setObjects(*((_C,_F),(_C,_G),(_C,_E)))
if mibBuilder.loadTexts:cnRPSTrapMsg.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cnRPSMib':cnRPSMib,'cnRPSTable':cnRPSTable,'cnRPSTableEntry':cnRPSTableEntry,_E:cnRPSIndex,'cnRPSMaximumVoltage':cnRPSMaximumVoltage,'cnRPSMaximumCurrent':cnRPSMaximumCurrent,_F:cnRPSMaximumWatts,_G:cnRPSStatus,'cnRPSCurrentInputVoltage':cnRPSCurrentInputVoltage,'cnRPSTrapMsg':cnRPSTrapMsg})