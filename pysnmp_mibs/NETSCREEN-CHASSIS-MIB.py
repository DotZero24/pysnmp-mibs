_G='nsSlotId'
_F='nsTemperatureId'
_E='nsFanId'
_D='nsPowerId'
_C='NETSCREEN-CHASSIS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreen,=mibBuilder.importSymbols('NETSCREEN-SMI','netscreen')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
netscreenChassis=ModuleIdentity((1,3,6,1,4,1,3224,21))
_NsPowerTable_Object=MibTable
nsPowerTable=_NsPowerTable_Object((1,3,6,1,4,1,3224,21,1))
if mibBuilder.loadTexts:nsPowerTable.setStatus(_A)
_NsPowerEntry_Object=MibTableRow
nsPowerEntry=_NsPowerEntry_Object((1,3,6,1,4,1,3224,21,1,1))
nsPowerEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:nsPowerEntry.setStatus(_A)
_NsPowerId_Type=Integer32
_NsPowerId_Object=MibTableColumn
nsPowerId=_NsPowerId_Object((1,3,6,1,4,1,3224,21,1,1,1),_NsPowerId_Type())
nsPowerId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPowerId.setStatus(_A)
_NsPowerStatus_Type=Integer32
_NsPowerStatus_Object=MibTableColumn
nsPowerStatus=_NsPowerStatus_Object((1,3,6,1,4,1,3224,21,1,1,2),_NsPowerStatus_Type())
nsPowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPowerStatus.setStatus(_A)
_NsPowerDesc_Type=DisplayString
_NsPowerDesc_Object=MibTableColumn
nsPowerDesc=_NsPowerDesc_Object((1,3,6,1,4,1,3224,21,1,1,3),_NsPowerDesc_Type())
nsPowerDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPowerDesc.setStatus(_A)
_NsFanTable_Object=MibTable
nsFanTable=_NsFanTable_Object((1,3,6,1,4,1,3224,21,2))
if mibBuilder.loadTexts:nsFanTable.setStatus(_A)
_NsFanEntry_Object=MibTableRow
nsFanEntry=_NsFanEntry_Object((1,3,6,1,4,1,3224,21,2,1))
nsFanEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:nsFanEntry.setStatus(_A)
_NsFanId_Type=Integer32
_NsFanId_Object=MibTableColumn
nsFanId=_NsFanId_Object((1,3,6,1,4,1,3224,21,2,1,1),_NsFanId_Type())
nsFanId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsFanId.setStatus(_A)
_NsFanStatus_Type=Integer32
_NsFanStatus_Object=MibTableColumn
nsFanStatus=_NsFanStatus_Object((1,3,6,1,4,1,3224,21,2,1,2),_NsFanStatus_Type())
nsFanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nsFanStatus.setStatus(_A)
_NsFanDesc_Type=DisplayString
_NsFanDesc_Object=MibTableColumn
nsFanDesc=_NsFanDesc_Object((1,3,6,1,4,1,3224,21,2,1,3),_NsFanDesc_Type())
nsFanDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:nsFanDesc.setStatus(_A)
_SysBatteryStatus_Type=Integer32
_SysBatteryStatus_Object=MibScalar
sysBatteryStatus=_SysBatteryStatus_Object((1,3,6,1,4,1,3224,21,3),_SysBatteryStatus_Type())
sysBatteryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sysBatteryStatus.setStatus(_A)
_NsTemperatureTable_Object=MibTable
nsTemperatureTable=_NsTemperatureTable_Object((1,3,6,1,4,1,3224,21,4))
if mibBuilder.loadTexts:nsTemperatureTable.setStatus(_A)
_NsTemperatureEntry_Object=MibTableRow
nsTemperatureEntry=_NsTemperatureEntry_Object((1,3,6,1,4,1,3224,21,4,1))
nsTemperatureEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:nsTemperatureEntry.setStatus(_A)
_NsTemperatureId_Type=Integer32
_NsTemperatureId_Object=MibTableColumn
nsTemperatureId=_NsTemperatureId_Object((1,3,6,1,4,1,3224,21,4,1,1),_NsTemperatureId_Type())
nsTemperatureId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsTemperatureId.setStatus(_A)
_NsTemperatureSlotId_Type=Integer32
_NsTemperatureSlotId_Object=MibTableColumn
nsTemperatureSlotId=_NsTemperatureSlotId_Object((1,3,6,1,4,1,3224,21,4,1,2),_NsTemperatureSlotId_Type())
nsTemperatureSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsTemperatureSlotId.setStatus(_A)
_NsTemperatureCur_Type=Integer32
_NsTemperatureCur_Object=MibTableColumn
nsTemperatureCur=_NsTemperatureCur_Object((1,3,6,1,4,1,3224,21,4,1,3),_NsTemperatureCur_Type())
nsTemperatureCur.setMaxAccess(_B)
if mibBuilder.loadTexts:nsTemperatureCur.setStatus(_A)
_NsTemperatureDesc_Type=DisplayString
_NsTemperatureDesc_Object=MibTableColumn
nsTemperatureDesc=_NsTemperatureDesc_Object((1,3,6,1,4,1,3224,21,4,1,4),_NsTemperatureDesc_Type())
nsTemperatureDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:nsTemperatureDesc.setStatus(_A)
_NsSlotTable_Object=MibTable
nsSlotTable=_NsSlotTable_Object((1,3,6,1,4,1,3224,21,5))
if mibBuilder.loadTexts:nsSlotTable.setStatus(_A)
_NsSlotEntry_Object=MibTableRow
nsSlotEntry=_NsSlotEntry_Object((1,3,6,1,4,1,3224,21,5,1))
nsSlotEntry.setIndexNames((0,_C,_G),(0,_C,'nsSubSlotId'))
if mibBuilder.loadTexts:nsSlotEntry.setStatus(_A)
_NsSlotId_Type=Integer32
_NsSlotId_Object=MibTableColumn
nsSlotId=_NsSlotId_Object((1,3,6,1,4,1,3224,21,5,1,1),_NsSlotId_Type())
nsSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSlotId.setStatus(_A)
_NsSlotType_Type=DisplayString
_NsSlotType_Object=MibTableColumn
nsSlotType=_NsSlotType_Object((1,3,6,1,4,1,3224,21,5,1,2),_NsSlotType_Type())
nsSlotType.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSlotType.setStatus(_A)
_NsSlotStatus_Type=Integer32
_NsSlotStatus_Object=MibTableColumn
nsSlotStatus=_NsSlotStatus_Object((1,3,6,1,4,1,3224,21,5,1,3),_NsSlotStatus_Type())
nsSlotStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSlotStatus.setStatus(_A)
_NsSlotSN_Type=DisplayString
_NsSlotSN_Object=MibTableColumn
nsSlotSN=_NsSlotSN_Object((1,3,6,1,4,1,3224,21,5,1,4),_NsSlotSN_Type())
nsSlotSN.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSlotSN.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'netscreenChassis':netscreenChassis,'nsPowerTable':nsPowerTable,'nsPowerEntry':nsPowerEntry,_D:nsPowerId,'nsPowerStatus':nsPowerStatus,'nsPowerDesc':nsPowerDesc,'nsFanTable':nsFanTable,'nsFanEntry':nsFanEntry,_E:nsFanId,'nsFanStatus':nsFanStatus,'nsFanDesc':nsFanDesc,'sysBatteryStatus':sysBatteryStatus,'nsTemperatureTable':nsTemperatureTable,'nsTemperatureEntry':nsTemperatureEntry,_F:nsTemperatureId,'nsTemperatureSlotId':nsTemperatureSlotId,'nsTemperatureCur':nsTemperatureCur,'nsTemperatureDesc':nsTemperatureDesc,'nsSlotTable':nsSlotTable,'nsSlotEntry':nsSlotEntry,_G:nsSlotId,'nsSlotType':nsSlotType,'nsSlotStatus':nsSlotStatus,'nsSlotSN':nsSlotSN})