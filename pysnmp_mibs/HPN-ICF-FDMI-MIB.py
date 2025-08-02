_J='hpnicfFdmiHbaPortId'
_I='OctetString'
_H='not-accessible'
_G='hpnicfFdmiHbaInfoId'
_F='hpnicfFdmiHbaInfoFabricIndex'
_E='fcmInstanceIndex'
_D='FC-MGMT-MIB'
_C='HPN-ICF-FDMI-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
FcNameIdOrZero,fcmInstanceIndex=mibBuilder.importSymbols(_D,'FcNameIdOrZero',_E)
hpnicfSan,=mibBuilder.importSymbols('HPN-ICF-VSAN-MIB','hpnicfSan')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
T11FabricIndex,=mibBuilder.importSymbols('T11-TC-MIB','T11FabricIndex')
hpnicfFdmi=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,7))
if mibBuilder.loadTexts:hpnicfFdmi.setRevisions(('2012-06-18 00:00',))
_HpnicfFdmiObjects_ObjectIdentity=ObjectIdentity
hpnicfFdmiObjects=_HpnicfFdmiObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,7,1))
_HpnicfFdmiInfo_ObjectIdentity=ObjectIdentity
hpnicfFdmiInfo=_HpnicfFdmiInfo_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,7,1,1))
_HpnicfFdmiHbaInfoTable_Object=MibTable
hpnicfFdmiHbaInfoTable=_HpnicfFdmiHbaInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,7,1,1,1))
if mibBuilder.loadTexts:hpnicfFdmiHbaInfoTable.setStatus(_A)
_HpnicfFdmiHbaInfoEntry_Object=MibTableRow
hpnicfFdmiHbaInfoEntry=_HpnicfFdmiHbaInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,7,1,1,1,1))
hpnicfFdmiHbaInfoEntry.setIndexNames((0,_D,_E),(0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:hpnicfFdmiHbaInfoEntry.setStatus(_A)
_HpnicfFdmiHbaInfoFabricIndex_Type=T11FabricIndex
_HpnicfFdmiHbaInfoFabricIndex_Object=MibTableColumn
hpnicfFdmiHbaInfoFabricIndex=_HpnicfFdmiHbaInfoFabricIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,7,1,1,1,1,1),_HpnicfFdmiHbaInfoFabricIndex_Type())
hpnicfFdmiHbaInfoFabricIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfFdmiHbaInfoFabricIndex.setStatus(_A)
_HpnicfFdmiHbaInfoId_Type=FcNameIdOrZero
_HpnicfFdmiHbaInfoId_Object=MibTableColumn
hpnicfFdmiHbaInfoId=_HpnicfFdmiHbaInfoId_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,7,1,1,1,1,2),_HpnicfFdmiHbaInfoId_Type())
hpnicfFdmiHbaInfoId.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfFdmiHbaInfoId.setStatus(_A)
_HpnicfFdmiHbaInfoNodeName_Type=FcNameIdOrZero
_HpnicfFdmiHbaInfoNodeName_Object=MibTableColumn
hpnicfFdmiHbaInfoNodeName=_HpnicfFdmiHbaInfoNodeName_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,7,1,1,1,1,3),_HpnicfFdmiHbaInfoNodeName_Type())
hpnicfFdmiHbaInfoNodeName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFdmiHbaInfoNodeName.setStatus(_A)
_HpnicfFdmiHbaInfoMfg_Type=SnmpAdminString
_HpnicfFdmiHbaInfoMfg_Object=MibTableColumn
hpnicfFdmiHbaInfoMfg=_HpnicfFdmiHbaInfoMfg_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,7,1,1,1,1,4),_HpnicfFdmiHbaInfoMfg_Type())
hpnicfFdmiHbaInfoMfg.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFdmiHbaInfoMfg.setStatus(_A)
_HpnicfFdmiHbaInfoSn_Type=SnmpAdminString
_HpnicfFdmiHbaInfoSn_Object=MibTableColumn
hpnicfFdmiHbaInfoSn=_HpnicfFdmiHbaInfoSn_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,7,1,1,1,1,5),_HpnicfFdmiHbaInfoSn_Type())
hpnicfFdmiHbaInfoSn.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFdmiHbaInfoSn.setStatus(_A)
_HpnicfFdmiHbaInfoModel_Type=SnmpAdminString
_HpnicfFdmiHbaInfoModel_Object=MibTableColumn
hpnicfFdmiHbaInfoModel=_HpnicfFdmiHbaInfoModel_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,7,1,1,1,1,6),_HpnicfFdmiHbaInfoModel_Type())
hpnicfFdmiHbaInfoModel.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFdmiHbaInfoModel.setStatus(_A)
_HpnicfFdmiHbaInfoModelDescr_Type=SnmpAdminString
_HpnicfFdmiHbaInfoModelDescr_Object=MibTableColumn
hpnicfFdmiHbaInfoModelDescr=_HpnicfFdmiHbaInfoModelDescr_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,7,1,1,1,1,7),_HpnicfFdmiHbaInfoModelDescr_Type())
hpnicfFdmiHbaInfoModelDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFdmiHbaInfoModelDescr.setStatus(_A)
_HpnicfFdmiHbaInfoHwVer_Type=SnmpAdminString
_HpnicfFdmiHbaInfoHwVer_Object=MibTableColumn
hpnicfFdmiHbaInfoHwVer=_HpnicfFdmiHbaInfoHwVer_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,7,1,1,1,1,8),_HpnicfFdmiHbaInfoHwVer_Type())
hpnicfFdmiHbaInfoHwVer.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFdmiHbaInfoHwVer.setStatus(_A)
_HpnicfFdmiHbaInfoDriverVer_Type=SnmpAdminString
_HpnicfFdmiHbaInfoDriverVer_Object=MibTableColumn
hpnicfFdmiHbaInfoDriverVer=_HpnicfFdmiHbaInfoDriverVer_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,7,1,1,1,1,9),_HpnicfFdmiHbaInfoDriverVer_Type())
hpnicfFdmiHbaInfoDriverVer.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFdmiHbaInfoDriverVer.setStatus(_A)
_HpnicfFdmiHbaInfoOptROMVer_Type=SnmpAdminString
_HpnicfFdmiHbaInfoOptROMVer_Object=MibTableColumn
hpnicfFdmiHbaInfoOptROMVer=_HpnicfFdmiHbaInfoOptROMVer_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,7,1,1,1,1,10),_HpnicfFdmiHbaInfoOptROMVer_Type())
hpnicfFdmiHbaInfoOptROMVer.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFdmiHbaInfoOptROMVer.setStatus(_A)
_HpnicfFdmiHbaInfoFwVer_Type=SnmpAdminString
_HpnicfFdmiHbaInfoFwVer_Object=MibTableColumn
hpnicfFdmiHbaInfoFwVer=_HpnicfFdmiHbaInfoFwVer_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,7,1,1,1,1,11),_HpnicfFdmiHbaInfoFwVer_Type())
hpnicfFdmiHbaInfoFwVer.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFdmiHbaInfoFwVer.setStatus(_A)
_HpnicfFdmiHbaInfoOSInfo_Type=SnmpAdminString
_HpnicfFdmiHbaInfoOSInfo_Object=MibTableColumn
hpnicfFdmiHbaInfoOSInfo=_HpnicfFdmiHbaInfoOSInfo_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,7,1,1,1,1,12),_HpnicfFdmiHbaInfoOSInfo_Type())
hpnicfFdmiHbaInfoOSInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFdmiHbaInfoOSInfo.setStatus(_A)
_HpnicfFdmiHbaInfoMaxCTPayload_Type=Unsigned32
_HpnicfFdmiHbaInfoMaxCTPayload_Object=MibTableColumn
hpnicfFdmiHbaInfoMaxCTPayload=_HpnicfFdmiHbaInfoMaxCTPayload_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,7,1,1,1,1,13),_HpnicfFdmiHbaInfoMaxCTPayload_Type())
hpnicfFdmiHbaInfoMaxCTPayload.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFdmiHbaInfoMaxCTPayload.setStatus(_A)
_HpnicfFdmiHbaPortTable_Object=MibTable
hpnicfFdmiHbaPortTable=_HpnicfFdmiHbaPortTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,7,1,1,2))
if mibBuilder.loadTexts:hpnicfFdmiHbaPortTable.setStatus(_A)
_HpnicfFdmiHbaPortEntry_Object=MibTableRow
hpnicfFdmiHbaPortEntry=_HpnicfFdmiHbaPortEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,7,1,1,2,1))
hpnicfFdmiHbaPortEntry.setIndexNames((0,_D,_E),(0,_C,_F),(0,_C,_G),(0,_C,_J))
if mibBuilder.loadTexts:hpnicfFdmiHbaPortEntry.setStatus(_A)
_HpnicfFdmiHbaPortId_Type=FcNameIdOrZero
_HpnicfFdmiHbaPortId_Object=MibTableColumn
hpnicfFdmiHbaPortId=_HpnicfFdmiHbaPortId_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,7,1,1,2,1,1),_HpnicfFdmiHbaPortId_Type())
hpnicfFdmiHbaPortId.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfFdmiHbaPortId.setStatus(_A)
class _HpnicfFdmiHbaPortSupportedFC4Type_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(32,32))
_HpnicfFdmiHbaPortSupportedFC4Type_Type.__name__=_I
_HpnicfFdmiHbaPortSupportedFC4Type_Object=MibTableColumn
hpnicfFdmiHbaPortSupportedFC4Type=_HpnicfFdmiHbaPortSupportedFC4Type_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,7,1,1,2,1,2),_HpnicfFdmiHbaPortSupportedFC4Type_Type())
hpnicfFdmiHbaPortSupportedFC4Type.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFdmiHbaPortSupportedFC4Type.setStatus(_A)
_HpnicfFdmiHbaPortSupportedSpeed_Type=Unsigned32
_HpnicfFdmiHbaPortSupportedSpeed_Object=MibTableColumn
hpnicfFdmiHbaPortSupportedSpeed=_HpnicfFdmiHbaPortSupportedSpeed_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,7,1,1,2,1,3),_HpnicfFdmiHbaPortSupportedSpeed_Type())
hpnicfFdmiHbaPortSupportedSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFdmiHbaPortSupportedSpeed.setStatus(_A)
_HpnicfFdmiHbaPortCurrentSpeed_Type=Unsigned32
_HpnicfFdmiHbaPortCurrentSpeed_Object=MibTableColumn
hpnicfFdmiHbaPortCurrentSpeed=_HpnicfFdmiHbaPortCurrentSpeed_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,7,1,1,2,1,4),_HpnicfFdmiHbaPortCurrentSpeed_Type())
hpnicfFdmiHbaPortCurrentSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFdmiHbaPortCurrentSpeed.setStatus(_A)
_HpnicfFdmiHbaPortMaxFrameSize_Type=Unsigned32
_HpnicfFdmiHbaPortMaxFrameSize_Object=MibTableColumn
hpnicfFdmiHbaPortMaxFrameSize=_HpnicfFdmiHbaPortMaxFrameSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,7,1,1,2,1,5),_HpnicfFdmiHbaPortMaxFrameSize_Type())
hpnicfFdmiHbaPortMaxFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFdmiHbaPortMaxFrameSize.setStatus(_A)
_HpnicfFdmiHbaPortOsDevName_Type=SnmpAdminString
_HpnicfFdmiHbaPortOsDevName_Object=MibTableColumn
hpnicfFdmiHbaPortOsDevName=_HpnicfFdmiHbaPortOsDevName_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,7,1,1,2,1,6),_HpnicfFdmiHbaPortOsDevName_Type())
hpnicfFdmiHbaPortOsDevName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFdmiHbaPortOsDevName.setStatus(_A)
_HpnicfFdmiHbaPortHostName_Type=SnmpAdminString
_HpnicfFdmiHbaPortHostName_Object=MibTableColumn
hpnicfFdmiHbaPortHostName=_HpnicfFdmiHbaPortHostName_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,7,1,1,2,1,7),_HpnicfFdmiHbaPortHostName_Type())
hpnicfFdmiHbaPortHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFdmiHbaPortHostName.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'hpnicfFdmi':hpnicfFdmi,'hpnicfFdmiObjects':hpnicfFdmiObjects,'hpnicfFdmiInfo':hpnicfFdmiInfo,'hpnicfFdmiHbaInfoTable':hpnicfFdmiHbaInfoTable,'hpnicfFdmiHbaInfoEntry':hpnicfFdmiHbaInfoEntry,_F:hpnicfFdmiHbaInfoFabricIndex,_G:hpnicfFdmiHbaInfoId,'hpnicfFdmiHbaInfoNodeName':hpnicfFdmiHbaInfoNodeName,'hpnicfFdmiHbaInfoMfg':hpnicfFdmiHbaInfoMfg,'hpnicfFdmiHbaInfoSn':hpnicfFdmiHbaInfoSn,'hpnicfFdmiHbaInfoModel':hpnicfFdmiHbaInfoModel,'hpnicfFdmiHbaInfoModelDescr':hpnicfFdmiHbaInfoModelDescr,'hpnicfFdmiHbaInfoHwVer':hpnicfFdmiHbaInfoHwVer,'hpnicfFdmiHbaInfoDriverVer':hpnicfFdmiHbaInfoDriverVer,'hpnicfFdmiHbaInfoOptROMVer':hpnicfFdmiHbaInfoOptROMVer,'hpnicfFdmiHbaInfoFwVer':hpnicfFdmiHbaInfoFwVer,'hpnicfFdmiHbaInfoOSInfo':hpnicfFdmiHbaInfoOSInfo,'hpnicfFdmiHbaInfoMaxCTPayload':hpnicfFdmiHbaInfoMaxCTPayload,'hpnicfFdmiHbaPortTable':hpnicfFdmiHbaPortTable,'hpnicfFdmiHbaPortEntry':hpnicfFdmiHbaPortEntry,_J:hpnicfFdmiHbaPortId,'hpnicfFdmiHbaPortSupportedFC4Type':hpnicfFdmiHbaPortSupportedFC4Type,'hpnicfFdmiHbaPortSupportedSpeed':hpnicfFdmiHbaPortSupportedSpeed,'hpnicfFdmiHbaPortCurrentSpeed':hpnicfFdmiHbaPortCurrentSpeed,'hpnicfFdmiHbaPortMaxFrameSize':hpnicfFdmiHbaPortMaxFrameSize,'hpnicfFdmiHbaPortOsDevName':hpnicfFdmiHbaPortOsDevName,'hpnicfFdmiHbaPortHostName':hpnicfFdmiHbaPortHostName})