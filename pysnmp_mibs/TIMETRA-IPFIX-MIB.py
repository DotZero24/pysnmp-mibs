_e='tmnxIpfixExportGroupV15v0'
_d='tmnxIpfixExpPlcyTemplateFormat'
_c='tmnxIpfixExpPlcyColTmplRefrshTo'
_b='tmnxIpfixExpPlcyColMtu'
_a='tmnxIpfixExpPlcyColSrcAddr'
_Z='tmnxIpfixExpPlcyColSrcAddrType'
_Y='tmnxIpfixExpPlcyColAdminState'
_X='tmnxIpfixExpPlcyColLastCh'
_W='tmnxIpfixExpPlcyColRowStatus'
_V='tmnxIpfixExpPlcyColTableCh'
_U='tmnxIpfixExpPlcyDescription'
_T='tmnxIpfixExpPlcyRowStatus'
_S='tmnxIpfixExpPlcyLastCh'
_R='tmnxIpfixExpPlcyTableCh'
_Q='tmnxIpfixExpPlcyColAddr'
_P='tmnxIpfixExpPlcyColAddrType'
_O='vRtrID'
_N='TIMETRA-VRTR-MIB'
_M='TmnxAdminState'
_L='TItemDescription'
_K='Integer32'
_J='InetAddressType'
_I='tmnxIpfixExportGroup'
_H='not-accessible'
_G='tmnxIpfixExpPlcyName'
_F='Unsigned32'
_E='InetAddress'
_D='read-only'
_C='read-create'
_B='TIMETRA-IPFIX-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_E,_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
TItemDescription,TNamedItem,TmnxAdminState=mibBuilder.importSymbols('TIMETRA-TC-MIB',_L,'TNamedItem',_M)
vRtrID,=mibBuilder.importSymbols(_N,_O)
timetraIpfixMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,3,78))
if mibBuilder.loadTexts:timetraIpfixMIBModule.setRevisions(('2012-02-28 00:00',))
_TmnxIpfixConformance_ObjectIdentity=ObjectIdentity
tmnxIpfixConformance=_TmnxIpfixConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,78))
_TmnxIpfixCompliances_ObjectIdentity=ObjectIdentity
tmnxIpfixCompliances=_TmnxIpfixCompliances_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,78,1))
_TmnxIpfixGroups_ObjectIdentity=ObjectIdentity
tmnxIpfixGroups=_TmnxIpfixGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,78,2))
_TmnxIpfix_ObjectIdentity=ObjectIdentity
tmnxIpfix=_TmnxIpfix_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,78))
_TmnxIpfixObjs_ObjectIdentity=ObjectIdentity
tmnxIpfixObjs=_TmnxIpfixObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,78,1))
_TmnxIpfixExportObjs_ObjectIdentity=ObjectIdentity
tmnxIpfixExportObjs=_TmnxIpfixExportObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,78,1,1))
_TmnxIpfixExpPlcyTable_Object=MibTable
tmnxIpfixExpPlcyTable=_TmnxIpfixExpPlcyTable_Object((1,3,6,1,4,1,6527,3,1,2,78,1,1,1))
if mibBuilder.loadTexts:tmnxIpfixExpPlcyTable.setStatus(_A)
_TmnxIpfixExpPlcyEntry_Object=MibTableRow
tmnxIpfixExpPlcyEntry=_TmnxIpfixExpPlcyEntry_Object((1,3,6,1,4,1,6527,3,1,2,78,1,1,1,1))
tmnxIpfixExpPlcyEntry.setIndexNames((1,_B,_G))
if mibBuilder.loadTexts:tmnxIpfixExpPlcyEntry.setStatus(_A)
_TmnxIpfixExpPlcyName_Type=TNamedItem
_TmnxIpfixExpPlcyName_Object=MibTableColumn
tmnxIpfixExpPlcyName=_TmnxIpfixExpPlcyName_Object((1,3,6,1,4,1,6527,3,1,2,78,1,1,1,1,1),_TmnxIpfixExpPlcyName_Type())
tmnxIpfixExpPlcyName.setMaxAccess(_H)
if mibBuilder.loadTexts:tmnxIpfixExpPlcyName.setStatus(_A)
_TmnxIpfixExpPlcyLastCh_Type=TimeStamp
_TmnxIpfixExpPlcyLastCh_Object=MibTableColumn
tmnxIpfixExpPlcyLastCh=_TmnxIpfixExpPlcyLastCh_Object((1,3,6,1,4,1,6527,3,1,2,78,1,1,1,1,2),_TmnxIpfixExpPlcyLastCh_Type())
tmnxIpfixExpPlcyLastCh.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxIpfixExpPlcyLastCh.setStatus(_A)
_TmnxIpfixExpPlcyRowStatus_Type=RowStatus
_TmnxIpfixExpPlcyRowStatus_Object=MibTableColumn
tmnxIpfixExpPlcyRowStatus=_TmnxIpfixExpPlcyRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,78,1,1,1,1,3),_TmnxIpfixExpPlcyRowStatus_Type())
tmnxIpfixExpPlcyRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxIpfixExpPlcyRowStatus.setStatus(_A)
class _TmnxIpfixExpPlcyDescription_Type(TItemDescription):defaultValue=OctetString('')
_TmnxIpfixExpPlcyDescription_Type.__name__=_L
_TmnxIpfixExpPlcyDescription_Object=MibTableColumn
tmnxIpfixExpPlcyDescription=_TmnxIpfixExpPlcyDescription_Object((1,3,6,1,4,1,6527,3,1,2,78,1,1,1,1,4),_TmnxIpfixExpPlcyDescription_Type())
tmnxIpfixExpPlcyDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxIpfixExpPlcyDescription.setStatus(_A)
class _TmnxIpfixExpPlcyTemplateFormat_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('format1',1),('format2',2)))
_TmnxIpfixExpPlcyTemplateFormat_Type.__name__=_K
_TmnxIpfixExpPlcyTemplateFormat_Object=MibTableColumn
tmnxIpfixExpPlcyTemplateFormat=_TmnxIpfixExpPlcyTemplateFormat_Object((1,3,6,1,4,1,6527,3,1,2,78,1,1,1,1,5),_TmnxIpfixExpPlcyTemplateFormat_Type())
tmnxIpfixExpPlcyTemplateFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxIpfixExpPlcyTemplateFormat.setStatus(_A)
_TmnxIpfixExpPlcyColTable_Object=MibTable
tmnxIpfixExpPlcyColTable=_TmnxIpfixExpPlcyColTable_Object((1,3,6,1,4,1,6527,3,1,2,78,1,1,2))
if mibBuilder.loadTexts:tmnxIpfixExpPlcyColTable.setStatus(_A)
_TmnxIpfixExpPlcyColEntry_Object=MibTableRow
tmnxIpfixExpPlcyColEntry=_TmnxIpfixExpPlcyColEntry_Object((1,3,6,1,4,1,6527,3,1,2,78,1,1,2,1))
tmnxIpfixExpPlcyColEntry.setIndexNames((0,_B,_G),(0,_N,_O),(0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:tmnxIpfixExpPlcyColEntry.setStatus(_A)
_TmnxIpfixExpPlcyColAddrType_Type=InetAddressType
_TmnxIpfixExpPlcyColAddrType_Object=MibTableColumn
tmnxIpfixExpPlcyColAddrType=_TmnxIpfixExpPlcyColAddrType_Object((1,3,6,1,4,1,6527,3,1,2,78,1,1,2,1,1),_TmnxIpfixExpPlcyColAddrType_Type())
tmnxIpfixExpPlcyColAddrType.setMaxAccess(_H)
if mibBuilder.loadTexts:tmnxIpfixExpPlcyColAddrType.setStatus(_A)
class _TmnxIpfixExpPlcyColAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TmnxIpfixExpPlcyColAddr_Type.__name__=_E
_TmnxIpfixExpPlcyColAddr_Object=MibTableColumn
tmnxIpfixExpPlcyColAddr=_TmnxIpfixExpPlcyColAddr_Object((1,3,6,1,4,1,6527,3,1,2,78,1,1,2,1,2),_TmnxIpfixExpPlcyColAddr_Type())
tmnxIpfixExpPlcyColAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:tmnxIpfixExpPlcyColAddr.setStatus(_A)
_TmnxIpfixExpPlcyColRowStatus_Type=RowStatus
_TmnxIpfixExpPlcyColRowStatus_Object=MibTableColumn
tmnxIpfixExpPlcyColRowStatus=_TmnxIpfixExpPlcyColRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,78,1,1,2,1,3),_TmnxIpfixExpPlcyColRowStatus_Type())
tmnxIpfixExpPlcyColRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxIpfixExpPlcyColRowStatus.setStatus(_A)
_TmnxIpfixExpPlcyColLastCh_Type=TimeStamp
_TmnxIpfixExpPlcyColLastCh_Object=MibTableColumn
tmnxIpfixExpPlcyColLastCh=_TmnxIpfixExpPlcyColLastCh_Object((1,3,6,1,4,1,6527,3,1,2,78,1,1,2,1,4),_TmnxIpfixExpPlcyColLastCh_Type())
tmnxIpfixExpPlcyColLastCh.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxIpfixExpPlcyColLastCh.setStatus(_A)
class _TmnxIpfixExpPlcyColAdminState_Type(TmnxAdminState):defaultValue=3
_TmnxIpfixExpPlcyColAdminState_Type.__name__=_M
_TmnxIpfixExpPlcyColAdminState_Object=MibTableColumn
tmnxIpfixExpPlcyColAdminState=_TmnxIpfixExpPlcyColAdminState_Object((1,3,6,1,4,1,6527,3,1,2,78,1,1,2,1,5),_TmnxIpfixExpPlcyColAdminState_Type())
tmnxIpfixExpPlcyColAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxIpfixExpPlcyColAdminState.setStatus(_A)
class _TmnxIpfixExpPlcyColSrcAddrType_Type(InetAddressType):defaultValue=0
_TmnxIpfixExpPlcyColSrcAddrType_Type.__name__=_J
_TmnxIpfixExpPlcyColSrcAddrType_Object=MibTableColumn
tmnxIpfixExpPlcyColSrcAddrType=_TmnxIpfixExpPlcyColSrcAddrType_Object((1,3,6,1,4,1,6527,3,1,2,78,1,1,2,1,6),_TmnxIpfixExpPlcyColSrcAddrType_Type())
tmnxIpfixExpPlcyColSrcAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxIpfixExpPlcyColSrcAddrType.setStatus(_A)
class _TmnxIpfixExpPlcyColSrcAddr_Type(InetAddress):defaultValue=OctetString('');subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TmnxIpfixExpPlcyColSrcAddr_Type.__name__=_E
_TmnxIpfixExpPlcyColSrcAddr_Object=MibTableColumn
tmnxIpfixExpPlcyColSrcAddr=_TmnxIpfixExpPlcyColSrcAddr_Object((1,3,6,1,4,1,6527,3,1,2,78,1,1,2,1,7),_TmnxIpfixExpPlcyColSrcAddr_Type())
tmnxIpfixExpPlcyColSrcAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxIpfixExpPlcyColSrcAddr.setStatus(_A)
class _TmnxIpfixExpPlcyColMtu_Type(Unsigned32):defaultValue=1500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(512,9212))
_TmnxIpfixExpPlcyColMtu_Type.__name__=_F
_TmnxIpfixExpPlcyColMtu_Object=MibTableColumn
tmnxIpfixExpPlcyColMtu=_TmnxIpfixExpPlcyColMtu_Object((1,3,6,1,4,1,6527,3,1,2,78,1,1,2,1,8),_TmnxIpfixExpPlcyColMtu_Type())
tmnxIpfixExpPlcyColMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxIpfixExpPlcyColMtu.setStatus(_A)
class _TmnxIpfixExpPlcyColTmplRefrshTo_Type(Unsigned32):defaultValue=600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(240,86400))
_TmnxIpfixExpPlcyColTmplRefrshTo_Type.__name__=_F
_TmnxIpfixExpPlcyColTmplRefrshTo_Object=MibTableColumn
tmnxIpfixExpPlcyColTmplRefrshTo=_TmnxIpfixExpPlcyColTmplRefrshTo_Object((1,3,6,1,4,1,6527,3,1,2,78,1,1,2,1,9),_TmnxIpfixExpPlcyColTmplRefrshTo_Type())
tmnxIpfixExpPlcyColTmplRefrshTo.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxIpfixExpPlcyColTmplRefrshTo.setStatus(_A)
if mibBuilder.loadTexts:tmnxIpfixExpPlcyColTmplRefrshTo.setUnits('seconds')
_TmnxIpfixExpPlcyTableCh_Type=TimeStamp
_TmnxIpfixExpPlcyTableCh_Object=MibScalar
tmnxIpfixExpPlcyTableCh=_TmnxIpfixExpPlcyTableCh_Object((1,3,6,1,4,1,6527,3,1,2,78,1,100),_TmnxIpfixExpPlcyTableCh_Type())
tmnxIpfixExpPlcyTableCh.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxIpfixExpPlcyTableCh.setStatus(_A)
_TmnxIpfixExpPlcyColTableCh_Type=TimeStamp
_TmnxIpfixExpPlcyColTableCh_Object=MibScalar
tmnxIpfixExpPlcyColTableCh=_TmnxIpfixExpPlcyColTableCh_Object((1,3,6,1,4,1,6527,3,1,2,78,1,101),_TmnxIpfixExpPlcyColTableCh_Type())
tmnxIpfixExpPlcyColTableCh.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxIpfixExpPlcyColTableCh.setStatus(_A)
_TmnxIpfixNotifyPrefix_ObjectIdentity=ObjectIdentity
tmnxIpfixNotifyPrefix=_TmnxIpfixNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,78))
_TmnxIpfixNotifications_ObjectIdentity=ObjectIdentity
tmnxIpfixNotifications=_TmnxIpfixNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,78,0))
tmnxIpfixExportGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,78,2,1))
tmnxIpfixExportGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:tmnxIpfixExportGroup.setStatus(_A)
tmnxIpfixExportGroupV15v0=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,78,2,2))
tmnxIpfixExportGroupV15v0.setObjects((_B,_d))
if mibBuilder.loadTexts:tmnxIpfixExportGroupV15v0.setStatus(_A)
tmnxIpfixCompliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,78,1,1))
tmnxIpfixCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:tmnxIpfixCompliance.setStatus('obsolete')
tmnxIpfixV15v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,78,1,2))
tmnxIpfixV15v0Compliance.setObjects(*((_B,_I),(_B,_e)))
if mibBuilder.loadTexts:tmnxIpfixV15v0Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'timetraIpfixMIBModule':timetraIpfixMIBModule,'tmnxIpfixConformance':tmnxIpfixConformance,'tmnxIpfixCompliances':tmnxIpfixCompliances,'tmnxIpfixCompliance':tmnxIpfixCompliance,'tmnxIpfixV15v0Compliance':tmnxIpfixV15v0Compliance,'tmnxIpfixGroups':tmnxIpfixGroups,_I:tmnxIpfixExportGroup,_e:tmnxIpfixExportGroupV15v0,'tmnxIpfix':tmnxIpfix,'tmnxIpfixObjs':tmnxIpfixObjs,'tmnxIpfixExportObjs':tmnxIpfixExportObjs,'tmnxIpfixExpPlcyTable':tmnxIpfixExpPlcyTable,'tmnxIpfixExpPlcyEntry':tmnxIpfixExpPlcyEntry,_G:tmnxIpfixExpPlcyName,_S:tmnxIpfixExpPlcyLastCh,_T:tmnxIpfixExpPlcyRowStatus,_U:tmnxIpfixExpPlcyDescription,_d:tmnxIpfixExpPlcyTemplateFormat,'tmnxIpfixExpPlcyColTable':tmnxIpfixExpPlcyColTable,'tmnxIpfixExpPlcyColEntry':tmnxIpfixExpPlcyColEntry,_P:tmnxIpfixExpPlcyColAddrType,_Q:tmnxIpfixExpPlcyColAddr,_W:tmnxIpfixExpPlcyColRowStatus,_X:tmnxIpfixExpPlcyColLastCh,_Y:tmnxIpfixExpPlcyColAdminState,_Z:tmnxIpfixExpPlcyColSrcAddrType,_a:tmnxIpfixExpPlcyColSrcAddr,_b:tmnxIpfixExpPlcyColMtu,_c:tmnxIpfixExpPlcyColTmplRefrshTo,_R:tmnxIpfixExpPlcyTableCh,_V:tmnxIpfixExpPlcyColTableCh,'tmnxIpfixNotifyPrefix':tmnxIpfixNotifyPrefix,'tmnxIpfixNotifications':tmnxIpfixNotifications})