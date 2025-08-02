_J='h3cFdmiHbaPortId'
_I='OctetString'
_H='not-accessible'
_G='h3cFdmiHbaInfoId'
_F='h3cFdmiHbaInfoFabricIndex'
_E='fcmInstanceIndex'
_D='FC-MGMT-MIB'
_C='H3C-FDMI-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
FcNameIdOrZero,fcmInstanceIndex=mibBuilder.importSymbols(_D,'FcNameIdOrZero',_E)
h3cSan,=mibBuilder.importSymbols('H3C-VSAN-MIB','h3cSan')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
T11FabricIndex,=mibBuilder.importSymbols('T11-TC-MIB','T11FabricIndex')
h3cFdmi=ModuleIdentity((1,3,6,1,4,1,2011,10,2,127,7))
if mibBuilder.loadTexts:h3cFdmi.setRevisions(('2012-06-18 00:00',))
_H3cFdmiObjects_ObjectIdentity=ObjectIdentity
h3cFdmiObjects=_H3cFdmiObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,7,1))
_H3cFdmiInfo_ObjectIdentity=ObjectIdentity
h3cFdmiInfo=_H3cFdmiInfo_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,7,1,1))
_H3cFdmiHbaInfoTable_Object=MibTable
h3cFdmiHbaInfoTable=_H3cFdmiHbaInfoTable_Object((1,3,6,1,4,1,2011,10,2,127,7,1,1,1))
if mibBuilder.loadTexts:h3cFdmiHbaInfoTable.setStatus(_A)
_H3cFdmiHbaInfoEntry_Object=MibTableRow
h3cFdmiHbaInfoEntry=_H3cFdmiHbaInfoEntry_Object((1,3,6,1,4,1,2011,10,2,127,7,1,1,1,1))
h3cFdmiHbaInfoEntry.setIndexNames((0,_D,_E),(0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:h3cFdmiHbaInfoEntry.setStatus(_A)
_H3cFdmiHbaInfoFabricIndex_Type=T11FabricIndex
_H3cFdmiHbaInfoFabricIndex_Object=MibTableColumn
h3cFdmiHbaInfoFabricIndex=_H3cFdmiHbaInfoFabricIndex_Object((1,3,6,1,4,1,2011,10,2,127,7,1,1,1,1,1),_H3cFdmiHbaInfoFabricIndex_Type())
h3cFdmiHbaInfoFabricIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cFdmiHbaInfoFabricIndex.setStatus(_A)
_H3cFdmiHbaInfoId_Type=FcNameIdOrZero
_H3cFdmiHbaInfoId_Object=MibTableColumn
h3cFdmiHbaInfoId=_H3cFdmiHbaInfoId_Object((1,3,6,1,4,1,2011,10,2,127,7,1,1,1,1,2),_H3cFdmiHbaInfoId_Type())
h3cFdmiHbaInfoId.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cFdmiHbaInfoId.setStatus(_A)
_H3cFdmiHbaInfoNodeName_Type=FcNameIdOrZero
_H3cFdmiHbaInfoNodeName_Object=MibTableColumn
h3cFdmiHbaInfoNodeName=_H3cFdmiHbaInfoNodeName_Object((1,3,6,1,4,1,2011,10,2,127,7,1,1,1,1,3),_H3cFdmiHbaInfoNodeName_Type())
h3cFdmiHbaInfoNodeName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFdmiHbaInfoNodeName.setStatus(_A)
_H3cFdmiHbaInfoMfg_Type=SnmpAdminString
_H3cFdmiHbaInfoMfg_Object=MibTableColumn
h3cFdmiHbaInfoMfg=_H3cFdmiHbaInfoMfg_Object((1,3,6,1,4,1,2011,10,2,127,7,1,1,1,1,4),_H3cFdmiHbaInfoMfg_Type())
h3cFdmiHbaInfoMfg.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFdmiHbaInfoMfg.setStatus(_A)
_H3cFdmiHbaInfoSn_Type=SnmpAdminString
_H3cFdmiHbaInfoSn_Object=MibTableColumn
h3cFdmiHbaInfoSn=_H3cFdmiHbaInfoSn_Object((1,3,6,1,4,1,2011,10,2,127,7,1,1,1,1,5),_H3cFdmiHbaInfoSn_Type())
h3cFdmiHbaInfoSn.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFdmiHbaInfoSn.setStatus(_A)
_H3cFdmiHbaInfoModel_Type=SnmpAdminString
_H3cFdmiHbaInfoModel_Object=MibTableColumn
h3cFdmiHbaInfoModel=_H3cFdmiHbaInfoModel_Object((1,3,6,1,4,1,2011,10,2,127,7,1,1,1,1,6),_H3cFdmiHbaInfoModel_Type())
h3cFdmiHbaInfoModel.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFdmiHbaInfoModel.setStatus(_A)
_H3cFdmiHbaInfoModelDescr_Type=SnmpAdminString
_H3cFdmiHbaInfoModelDescr_Object=MibTableColumn
h3cFdmiHbaInfoModelDescr=_H3cFdmiHbaInfoModelDescr_Object((1,3,6,1,4,1,2011,10,2,127,7,1,1,1,1,7),_H3cFdmiHbaInfoModelDescr_Type())
h3cFdmiHbaInfoModelDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFdmiHbaInfoModelDescr.setStatus(_A)
_H3cFdmiHbaInfoHwVer_Type=SnmpAdminString
_H3cFdmiHbaInfoHwVer_Object=MibTableColumn
h3cFdmiHbaInfoHwVer=_H3cFdmiHbaInfoHwVer_Object((1,3,6,1,4,1,2011,10,2,127,7,1,1,1,1,8),_H3cFdmiHbaInfoHwVer_Type())
h3cFdmiHbaInfoHwVer.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFdmiHbaInfoHwVer.setStatus(_A)
_H3cFdmiHbaInfoDriverVer_Type=SnmpAdminString
_H3cFdmiHbaInfoDriverVer_Object=MibTableColumn
h3cFdmiHbaInfoDriverVer=_H3cFdmiHbaInfoDriverVer_Object((1,3,6,1,4,1,2011,10,2,127,7,1,1,1,1,9),_H3cFdmiHbaInfoDriverVer_Type())
h3cFdmiHbaInfoDriverVer.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFdmiHbaInfoDriverVer.setStatus(_A)
_H3cFdmiHbaInfoOptROMVer_Type=SnmpAdminString
_H3cFdmiHbaInfoOptROMVer_Object=MibTableColumn
h3cFdmiHbaInfoOptROMVer=_H3cFdmiHbaInfoOptROMVer_Object((1,3,6,1,4,1,2011,10,2,127,7,1,1,1,1,10),_H3cFdmiHbaInfoOptROMVer_Type())
h3cFdmiHbaInfoOptROMVer.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFdmiHbaInfoOptROMVer.setStatus(_A)
_H3cFdmiHbaInfoFwVer_Type=SnmpAdminString
_H3cFdmiHbaInfoFwVer_Object=MibTableColumn
h3cFdmiHbaInfoFwVer=_H3cFdmiHbaInfoFwVer_Object((1,3,6,1,4,1,2011,10,2,127,7,1,1,1,1,11),_H3cFdmiHbaInfoFwVer_Type())
h3cFdmiHbaInfoFwVer.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFdmiHbaInfoFwVer.setStatus(_A)
_H3cFdmiHbaInfoOSInfo_Type=SnmpAdminString
_H3cFdmiHbaInfoOSInfo_Object=MibTableColumn
h3cFdmiHbaInfoOSInfo=_H3cFdmiHbaInfoOSInfo_Object((1,3,6,1,4,1,2011,10,2,127,7,1,1,1,1,12),_H3cFdmiHbaInfoOSInfo_Type())
h3cFdmiHbaInfoOSInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFdmiHbaInfoOSInfo.setStatus(_A)
_H3cFdmiHbaInfoMaxCTPayload_Type=Unsigned32
_H3cFdmiHbaInfoMaxCTPayload_Object=MibTableColumn
h3cFdmiHbaInfoMaxCTPayload=_H3cFdmiHbaInfoMaxCTPayload_Object((1,3,6,1,4,1,2011,10,2,127,7,1,1,1,1,13),_H3cFdmiHbaInfoMaxCTPayload_Type())
h3cFdmiHbaInfoMaxCTPayload.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFdmiHbaInfoMaxCTPayload.setStatus(_A)
_H3cFdmiHbaPortTable_Object=MibTable
h3cFdmiHbaPortTable=_H3cFdmiHbaPortTable_Object((1,3,6,1,4,1,2011,10,2,127,7,1,1,2))
if mibBuilder.loadTexts:h3cFdmiHbaPortTable.setStatus(_A)
_H3cFdmiHbaPortEntry_Object=MibTableRow
h3cFdmiHbaPortEntry=_H3cFdmiHbaPortEntry_Object((1,3,6,1,4,1,2011,10,2,127,7,1,1,2,1))
h3cFdmiHbaPortEntry.setIndexNames((0,_D,_E),(0,_C,_F),(0,_C,_G),(0,_C,_J))
if mibBuilder.loadTexts:h3cFdmiHbaPortEntry.setStatus(_A)
_H3cFdmiHbaPortId_Type=FcNameIdOrZero
_H3cFdmiHbaPortId_Object=MibTableColumn
h3cFdmiHbaPortId=_H3cFdmiHbaPortId_Object((1,3,6,1,4,1,2011,10,2,127,7,1,1,2,1,1),_H3cFdmiHbaPortId_Type())
h3cFdmiHbaPortId.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cFdmiHbaPortId.setStatus(_A)
class _H3cFdmiHbaPortSupportedFC4Type_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(32,32))
_H3cFdmiHbaPortSupportedFC4Type_Type.__name__=_I
_H3cFdmiHbaPortSupportedFC4Type_Object=MibTableColumn
h3cFdmiHbaPortSupportedFC4Type=_H3cFdmiHbaPortSupportedFC4Type_Object((1,3,6,1,4,1,2011,10,2,127,7,1,1,2,1,2),_H3cFdmiHbaPortSupportedFC4Type_Type())
h3cFdmiHbaPortSupportedFC4Type.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFdmiHbaPortSupportedFC4Type.setStatus(_A)
_H3cFdmiHbaPortSupportedSpeed_Type=Unsigned32
_H3cFdmiHbaPortSupportedSpeed_Object=MibTableColumn
h3cFdmiHbaPortSupportedSpeed=_H3cFdmiHbaPortSupportedSpeed_Object((1,3,6,1,4,1,2011,10,2,127,7,1,1,2,1,3),_H3cFdmiHbaPortSupportedSpeed_Type())
h3cFdmiHbaPortSupportedSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFdmiHbaPortSupportedSpeed.setStatus(_A)
_H3cFdmiHbaPortCurrentSpeed_Type=Unsigned32
_H3cFdmiHbaPortCurrentSpeed_Object=MibTableColumn
h3cFdmiHbaPortCurrentSpeed=_H3cFdmiHbaPortCurrentSpeed_Object((1,3,6,1,4,1,2011,10,2,127,7,1,1,2,1,4),_H3cFdmiHbaPortCurrentSpeed_Type())
h3cFdmiHbaPortCurrentSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFdmiHbaPortCurrentSpeed.setStatus(_A)
_H3cFdmiHbaPortMaxFrameSize_Type=Unsigned32
_H3cFdmiHbaPortMaxFrameSize_Object=MibTableColumn
h3cFdmiHbaPortMaxFrameSize=_H3cFdmiHbaPortMaxFrameSize_Object((1,3,6,1,4,1,2011,10,2,127,7,1,1,2,1,5),_H3cFdmiHbaPortMaxFrameSize_Type())
h3cFdmiHbaPortMaxFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFdmiHbaPortMaxFrameSize.setStatus(_A)
_H3cFdmiHbaPortOsDevName_Type=SnmpAdminString
_H3cFdmiHbaPortOsDevName_Object=MibTableColumn
h3cFdmiHbaPortOsDevName=_H3cFdmiHbaPortOsDevName_Object((1,3,6,1,4,1,2011,10,2,127,7,1,1,2,1,6),_H3cFdmiHbaPortOsDevName_Type())
h3cFdmiHbaPortOsDevName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFdmiHbaPortOsDevName.setStatus(_A)
_H3cFdmiHbaPortHostName_Type=SnmpAdminString
_H3cFdmiHbaPortHostName_Object=MibTableColumn
h3cFdmiHbaPortHostName=_H3cFdmiHbaPortHostName_Object((1,3,6,1,4,1,2011,10,2,127,7,1,1,2,1,7),_H3cFdmiHbaPortHostName_Type())
h3cFdmiHbaPortHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFdmiHbaPortHostName.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'h3cFdmi':h3cFdmi,'h3cFdmiObjects':h3cFdmiObjects,'h3cFdmiInfo':h3cFdmiInfo,'h3cFdmiHbaInfoTable':h3cFdmiHbaInfoTable,'h3cFdmiHbaInfoEntry':h3cFdmiHbaInfoEntry,_F:h3cFdmiHbaInfoFabricIndex,_G:h3cFdmiHbaInfoId,'h3cFdmiHbaInfoNodeName':h3cFdmiHbaInfoNodeName,'h3cFdmiHbaInfoMfg':h3cFdmiHbaInfoMfg,'h3cFdmiHbaInfoSn':h3cFdmiHbaInfoSn,'h3cFdmiHbaInfoModel':h3cFdmiHbaInfoModel,'h3cFdmiHbaInfoModelDescr':h3cFdmiHbaInfoModelDescr,'h3cFdmiHbaInfoHwVer':h3cFdmiHbaInfoHwVer,'h3cFdmiHbaInfoDriverVer':h3cFdmiHbaInfoDriverVer,'h3cFdmiHbaInfoOptROMVer':h3cFdmiHbaInfoOptROMVer,'h3cFdmiHbaInfoFwVer':h3cFdmiHbaInfoFwVer,'h3cFdmiHbaInfoOSInfo':h3cFdmiHbaInfoOSInfo,'h3cFdmiHbaInfoMaxCTPayload':h3cFdmiHbaInfoMaxCTPayload,'h3cFdmiHbaPortTable':h3cFdmiHbaPortTable,'h3cFdmiHbaPortEntry':h3cFdmiHbaPortEntry,_J:h3cFdmiHbaPortId,'h3cFdmiHbaPortSupportedFC4Type':h3cFdmiHbaPortSupportedFC4Type,'h3cFdmiHbaPortSupportedSpeed':h3cFdmiHbaPortSupportedSpeed,'h3cFdmiHbaPortCurrentSpeed':h3cFdmiHbaPortCurrentSpeed,'h3cFdmiHbaPortMaxFrameSize':h3cFdmiHbaPortMaxFrameSize,'h3cFdmiHbaPortOsDevName':h3cFdmiHbaPortOsDevName,'h3cFdmiHbaPortHostName':h3cFdmiHbaPortHostName})