_H='optixWDMGetPsuBID'
_G='optixWDMGetFanBID'
_F='optixWDMGetBdInfoBID'
_E='OctetString'
_D='OPTIX-OSN908-FUNCTION-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
optixProvisionWDM,=mibBuilder.importSymbols('OPTIX-OID-MIB','optixProvisionWDM')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_OptixWDMFunction_ObjectIdentity=ObjectIdentity
optixWDMFunction=_OptixWDMFunction_ObjectIdentity((1,3,6,1,4,1,2011,2,25,4,70,10))
_OptixWDMBdinfo_ObjectIdentity=ObjectIdentity
optixWDMBdinfo=_OptixWDMBdinfo_ObjectIdentity((1,3,6,1,4,1,2011,2,25,4,70,10,20))
_OptixWDMGetBdInfoTable_Object=MibTable
optixWDMGetBdInfoTable=_OptixWDMGetBdInfoTable_Object((1,3,6,1,4,1,2011,2,25,4,70,10,20,10))
if mibBuilder.loadTexts:optixWDMGetBdInfoTable.setStatus(_A)
_OptixWDMGetBdInfoEntry_Object=MibTableRow
optixWDMGetBdInfoEntry=_OptixWDMGetBdInfoEntry_Object((1,3,6,1,4,1,2011,2,25,4,70,10,20,10,1))
optixWDMGetBdInfoEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:optixWDMGetBdInfoEntry.setStatus(_A)
class _OptixWDMGetBdInfoBID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_OptixWDMGetBdInfoBID_Type.__name__=_E
_OptixWDMGetBdInfoBID_Object=MibTableColumn
optixWDMGetBdInfoBID=_OptixWDMGetBdInfoBID_Object((1,3,6,1,4,1,2011,2,25,4,70,10,20,10,1,1),_OptixWDMGetBdInfoBID_Type())
optixWDMGetBdInfoBID.setMaxAccess(_B)
if mibBuilder.loadTexts:optixWDMGetBdInfoBID.setStatus(_A)
class _OptixWDMGetBdInfoData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4620))
_OptixWDMGetBdInfoData_Type.__name__=_E
_OptixWDMGetBdInfoData_Object=MibTableColumn
optixWDMGetBdInfoData=_OptixWDMGetBdInfoData_Object((1,3,6,1,4,1,2011,2,25,4,70,10,20,10,1,2),_OptixWDMGetBdInfoData_Type())
optixWDMGetBdInfoData.setMaxAccess(_B)
if mibBuilder.loadTexts:optixWDMGetBdInfoData.setStatus(_A)
_OptixWDMDeviceMgr_ObjectIdentity=ObjectIdentity
optixWDMDeviceMgr=_OptixWDMDeviceMgr_ObjectIdentity((1,3,6,1,4,1,2011,2,25,4,70,20))
_OptixWDMFanMgr_ObjectIdentity=ObjectIdentity
optixWDMFanMgr=_OptixWDMFanMgr_ObjectIdentity((1,3,6,1,4,1,2011,2,25,4,70,20,10))
_OptixWDMFanTable_Object=MibTable
optixWDMFanTable=_OptixWDMFanTable_Object((1,3,6,1,4,1,2011,2,25,4,70,20,10,10))
if mibBuilder.loadTexts:optixWDMFanTable.setStatus(_A)
_OptixWDMFanEntry_Object=MibTableRow
optixWDMFanEntry=_OptixWDMFanEntry_Object((1,3,6,1,4,1,2011,2,25,4,70,20,10,10,1))
optixWDMFanEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:optixWDMFanEntry.setStatus(_A)
class _OptixWDMGetFanBID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OptixWDMGetFanBID_Type.__name__=_C
_OptixWDMGetFanBID_Object=MibTableColumn
optixWDMGetFanBID=_OptixWDMGetFanBID_Object((1,3,6,1,4,1,2011,2,25,4,70,20,10,10,1,1),_OptixWDMGetFanBID_Type())
optixWDMGetFanBID.setMaxAccess(_B)
if mibBuilder.loadTexts:optixWDMGetFanBID.setStatus(_A)
class _OptixWDMGetFanSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,9,10,11)));namedValues=NamedValues(*(('low',1),('mid',2),('high',3),('stop',4),('auto-low',5),('auto-mid',6),('auto-high',7),('auto',9),('mid-low',10),('mid-high',11)))
_OptixWDMGetFanSpeed_Type.__name__=_C
_OptixWDMGetFanSpeed_Object=MibTableColumn
optixWDMGetFanSpeed=_OptixWDMGetFanSpeed_Object((1,3,6,1,4,1,2011,2,25,4,70,20,10,10,1,2),_OptixWDMGetFanSpeed_Type())
optixWDMGetFanSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:optixWDMGetFanSpeed.setStatus(_A)
_OptixWDMPsuMgr_ObjectIdentity=ObjectIdentity
optixWDMPsuMgr=_OptixWDMPsuMgr_ObjectIdentity((1,3,6,1,4,1,2011,2,25,4,70,20,20))
_OptixWDMPsuTable_Object=MibTable
optixWDMPsuTable=_OptixWDMPsuTable_Object((1,3,6,1,4,1,2011,2,25,4,70,20,20,10))
if mibBuilder.loadTexts:optixWDMPsuTable.setStatus(_A)
_OptixWDMPsuEntry_Object=MibTableRow
optixWDMPsuEntry=_OptixWDMPsuEntry_Object((1,3,6,1,4,1,2011,2,25,4,70,20,20,10,1))
optixWDMPsuEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:optixWDMPsuEntry.setStatus(_A)
class _OptixWDMGetPsuBID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OptixWDMGetPsuBID_Type.__name__=_C
_OptixWDMGetPsuBID_Object=MibTableColumn
optixWDMGetPsuBID=_OptixWDMGetPsuBID_Object((1,3,6,1,4,1,2011,2,25,4,70,20,20,10,1,1),_OptixWDMGetPsuBID_Type())
optixWDMGetPsuBID.setMaxAccess(_B)
if mibBuilder.loadTexts:optixWDMGetPsuBID.setStatus(_A)
class _OptixWDMGetPsuPowerConsumption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OptixWDMGetPsuPowerConsumption_Type.__name__=_C
_OptixWDMGetPsuPowerConsumption_Object=MibTableColumn
optixWDMGetPsuPowerConsumption=_OptixWDMGetPsuPowerConsumption_Object((1,3,6,1,4,1,2011,2,25,4,70,20,20,10,1,2),_OptixWDMGetPsuPowerConsumption_Type())
optixWDMGetPsuPowerConsumption.setMaxAccess(_B)
if mibBuilder.loadTexts:optixWDMGetPsuPowerConsumption.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'optixWDMFunction':optixWDMFunction,'optixWDMBdinfo':optixWDMBdinfo,'optixWDMGetBdInfoTable':optixWDMGetBdInfoTable,'optixWDMGetBdInfoEntry':optixWDMGetBdInfoEntry,_F:optixWDMGetBdInfoBID,'optixWDMGetBdInfoData':optixWDMGetBdInfoData,'optixWDMDeviceMgr':optixWDMDeviceMgr,'optixWDMFanMgr':optixWDMFanMgr,'optixWDMFanTable':optixWDMFanTable,'optixWDMFanEntry':optixWDMFanEntry,_G:optixWDMGetFanBID,'optixWDMGetFanSpeed':optixWDMGetFanSpeed,'optixWDMPsuMgr':optixWDMPsuMgr,'optixWDMPsuTable':optixWDMPsuTable,'optixWDMPsuEntry':optixWDMPsuEntry,_H:optixWDMGetPsuBID,'optixWDMGetPsuPowerConsumption':optixWDMGetPsuPowerConsumption})