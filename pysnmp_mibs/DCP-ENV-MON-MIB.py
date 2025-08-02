_F='dcpEnvMonFanIndex'
_E='dcpEnvMonPowerConsumptionIndex'
_D='dcpEnvMonTemperatureIndex'
_C='DCP-ENV-MON-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dcpGeneric,=mibBuilder.importSymbols('DCP-MIB','dcpGeneric')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
DcpTenths,FanMode,FanStatus=mibBuilder.importSymbols('SO-TC-MIB','DcpTenths','FanMode','FanStatus')
dcpEnv=ModuleIdentity((1,3,6,1,4,1,30826,2,2,6))
if mibBuilder.loadTexts:dcpEnv.setRevisions(('2023-03-30 18:00',))
_DcpEnvMon_ObjectIdentity=ObjectIdentity
dcpEnvMon=_DcpEnvMon_ObjectIdentity((1,3,6,1,4,1,30826,2,2,6,1))
_DcpEnvMonTemperature_ObjectIdentity=ObjectIdentity
dcpEnvMonTemperature=_DcpEnvMonTemperature_ObjectIdentity((1,3,6,1,4,1,30826,2,2,6,1,1))
_DcpEnvMonTemperatureObjects_ObjectIdentity=ObjectIdentity
dcpEnvMonTemperatureObjects=_DcpEnvMonTemperatureObjects_ObjectIdentity((1,3,6,1,4,1,30826,2,2,6,1,1,1))
_DcpEnvMonTemperatureTable_Object=MibTable
dcpEnvMonTemperatureTable=_DcpEnvMonTemperatureTable_Object((1,3,6,1,4,1,30826,2,2,6,1,1,1,1))
if mibBuilder.loadTexts:dcpEnvMonTemperatureTable.setStatus(_A)
_DcpEnvMonTemperatureEntry_Object=MibTableRow
dcpEnvMonTemperatureEntry=_DcpEnvMonTemperatureEntry_Object((1,3,6,1,4,1,30826,2,2,6,1,1,1,1,1))
dcpEnvMonTemperatureEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:dcpEnvMonTemperatureEntry.setStatus(_A)
_DcpEnvMonTemperatureIndex_Type=Unsigned32
_DcpEnvMonTemperatureIndex_Object=MibTableColumn
dcpEnvMonTemperatureIndex=_DcpEnvMonTemperatureIndex_Object((1,3,6,1,4,1,30826,2,2,6,1,1,1,1,1,1),_DcpEnvMonTemperatureIndex_Type())
dcpEnvMonTemperatureIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcpEnvMonTemperatureIndex.setStatus(_A)
_DcpEnvMonTemperatureDescription_Type=DisplayString
_DcpEnvMonTemperatureDescription_Object=MibTableColumn
dcpEnvMonTemperatureDescription=_DcpEnvMonTemperatureDescription_Object((1,3,6,1,4,1,30826,2,2,6,1,1,1,1,1,2),_DcpEnvMonTemperatureDescription_Type())
dcpEnvMonTemperatureDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:dcpEnvMonTemperatureDescription.setStatus(_A)
_DcpEnvMonTemperatureValue_Type=DcpTenths
_DcpEnvMonTemperatureValue_Object=MibTableColumn
dcpEnvMonTemperatureValue=_DcpEnvMonTemperatureValue_Object((1,3,6,1,4,1,30826,2,2,6,1,1,1,1,1,3),_DcpEnvMonTemperatureValue_Type())
dcpEnvMonTemperatureValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcpEnvMonTemperatureValue.setStatus(_A)
_DcpEnvMonPowerConsumption_ObjectIdentity=ObjectIdentity
dcpEnvMonPowerConsumption=_DcpEnvMonPowerConsumption_ObjectIdentity((1,3,6,1,4,1,30826,2,2,6,1,2))
_DcpEnvMonPowerConsumptionObjects_ObjectIdentity=ObjectIdentity
dcpEnvMonPowerConsumptionObjects=_DcpEnvMonPowerConsumptionObjects_ObjectIdentity((1,3,6,1,4,1,30826,2,2,6,1,2,1))
_DcpEnvMonPowerConsumptionTable_Object=MibTable
dcpEnvMonPowerConsumptionTable=_DcpEnvMonPowerConsumptionTable_Object((1,3,6,1,4,1,30826,2,2,6,1,2,1,1))
if mibBuilder.loadTexts:dcpEnvMonPowerConsumptionTable.setStatus(_A)
_DcpEnvMonPowerConsumptionEntry_Object=MibTableRow
dcpEnvMonPowerConsumptionEntry=_DcpEnvMonPowerConsumptionEntry_Object((1,3,6,1,4,1,30826,2,2,6,1,2,1,1,1))
dcpEnvMonPowerConsumptionEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:dcpEnvMonPowerConsumptionEntry.setStatus(_A)
_DcpEnvMonPowerConsumptionIndex_Type=Unsigned32
_DcpEnvMonPowerConsumptionIndex_Object=MibTableColumn
dcpEnvMonPowerConsumptionIndex=_DcpEnvMonPowerConsumptionIndex_Object((1,3,6,1,4,1,30826,2,2,6,1,2,1,1,1,1),_DcpEnvMonPowerConsumptionIndex_Type())
dcpEnvMonPowerConsumptionIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcpEnvMonPowerConsumptionIndex.setStatus(_A)
_DcpEnvMonPowerConsumptionDescription_Type=DisplayString
_DcpEnvMonPowerConsumptionDescription_Object=MibTableColumn
dcpEnvMonPowerConsumptionDescription=_DcpEnvMonPowerConsumptionDescription_Object((1,3,6,1,4,1,30826,2,2,6,1,2,1,1,1,2),_DcpEnvMonPowerConsumptionDescription_Type())
dcpEnvMonPowerConsumptionDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:dcpEnvMonPowerConsumptionDescription.setStatus(_A)
_DcpEnvMonPowerConsumptionValue_Type=Integer32
_DcpEnvMonPowerConsumptionValue_Object=MibTableColumn
dcpEnvMonPowerConsumptionValue=_DcpEnvMonPowerConsumptionValue_Object((1,3,6,1,4,1,30826,2,2,6,1,2,1,1,1,3),_DcpEnvMonPowerConsumptionValue_Type())
dcpEnvMonPowerConsumptionValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcpEnvMonPowerConsumptionValue.setStatus(_A)
_DcpEnvMonFan_ObjectIdentity=ObjectIdentity
dcpEnvMonFan=_DcpEnvMonFan_ObjectIdentity((1,3,6,1,4,1,30826,2,2,6,1,3))
_DcpEnvMonFanObjects_ObjectIdentity=ObjectIdentity
dcpEnvMonFanObjects=_DcpEnvMonFanObjects_ObjectIdentity((1,3,6,1,4,1,30826,2,2,6,1,3,1))
_DcpEnvMonFanTable_Object=MibTable
dcpEnvMonFanTable=_DcpEnvMonFanTable_Object((1,3,6,1,4,1,30826,2,2,6,1,3,1,1))
if mibBuilder.loadTexts:dcpEnvMonFanTable.setStatus(_A)
_DcpEnvMonFanEntry_Object=MibTableRow
dcpEnvMonFanEntry=_DcpEnvMonFanEntry_Object((1,3,6,1,4,1,30826,2,2,6,1,3,1,1,1))
dcpEnvMonFanEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:dcpEnvMonFanEntry.setStatus(_A)
_DcpEnvMonFanIndex_Type=Unsigned32
_DcpEnvMonFanIndex_Object=MibTableColumn
dcpEnvMonFanIndex=_DcpEnvMonFanIndex_Object((1,3,6,1,4,1,30826,2,2,6,1,3,1,1,1,1),_DcpEnvMonFanIndex_Type())
dcpEnvMonFanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcpEnvMonFanIndex.setStatus(_A)
_DcpEnvMonFanDescription_Type=DisplayString
_DcpEnvMonFanDescription_Object=MibTableColumn
dcpEnvMonFanDescription=_DcpEnvMonFanDescription_Object((1,3,6,1,4,1,30826,2,2,6,1,3,1,1,1,2),_DcpEnvMonFanDescription_Type())
dcpEnvMonFanDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:dcpEnvMonFanDescription.setStatus(_A)
_DcpEnvMonFanStatus_Type=FanStatus
_DcpEnvMonFanStatus_Object=MibTableColumn
dcpEnvMonFanStatus=_DcpEnvMonFanStatus_Object((1,3,6,1,4,1,30826,2,2,6,1,3,1,1,1,3),_DcpEnvMonFanStatus_Type())
dcpEnvMonFanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dcpEnvMonFanStatus.setStatus(_A)
_DcpEnvMonFanMode_Type=FanMode
_DcpEnvMonFanMode_Object=MibTableColumn
dcpEnvMonFanMode=_DcpEnvMonFanMode_Object((1,3,6,1,4,1,30826,2,2,6,1,3,1,1,1,4),_DcpEnvMonFanMode_Type())
dcpEnvMonFanMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dcpEnvMonFanMode.setStatus(_A)
_DcpEnvMonFanSpeed_Type=Unsigned32
_DcpEnvMonFanSpeed_Object=MibTableColumn
dcpEnvMonFanSpeed=_DcpEnvMonFanSpeed_Object((1,3,6,1,4,1,30826,2,2,6,1,3,1,1,1,5),_DcpEnvMonFanSpeed_Type())
dcpEnvMonFanSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:dcpEnvMonFanSpeed.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'dcpEnv':dcpEnv,'dcpEnvMon':dcpEnvMon,'dcpEnvMonTemperature':dcpEnvMonTemperature,'dcpEnvMonTemperatureObjects':dcpEnvMonTemperatureObjects,'dcpEnvMonTemperatureTable':dcpEnvMonTemperatureTable,'dcpEnvMonTemperatureEntry':dcpEnvMonTemperatureEntry,_D:dcpEnvMonTemperatureIndex,'dcpEnvMonTemperatureDescription':dcpEnvMonTemperatureDescription,'dcpEnvMonTemperatureValue':dcpEnvMonTemperatureValue,'dcpEnvMonPowerConsumption':dcpEnvMonPowerConsumption,'dcpEnvMonPowerConsumptionObjects':dcpEnvMonPowerConsumptionObjects,'dcpEnvMonPowerConsumptionTable':dcpEnvMonPowerConsumptionTable,'dcpEnvMonPowerConsumptionEntry':dcpEnvMonPowerConsumptionEntry,_E:dcpEnvMonPowerConsumptionIndex,'dcpEnvMonPowerConsumptionDescription':dcpEnvMonPowerConsumptionDescription,'dcpEnvMonPowerConsumptionValue':dcpEnvMonPowerConsumptionValue,'dcpEnvMonFan':dcpEnvMonFan,'dcpEnvMonFanObjects':dcpEnvMonFanObjects,'dcpEnvMonFanTable':dcpEnvMonFanTable,'dcpEnvMonFanEntry':dcpEnvMonFanEntry,_F:dcpEnvMonFanIndex,'dcpEnvMonFanDescription':dcpEnvMonFanDescription,'dcpEnvMonFanStatus':dcpEnvMonFanStatus,'dcpEnvMonFanMode':dcpEnvMonFanMode,'dcpEnvMonFanSpeed':dcpEnvMonFanSpeed})