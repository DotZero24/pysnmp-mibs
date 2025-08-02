_M='begemotNgHookHook'
_L='begemotNgHookNodeId'
_K='invalid'
_J='begemotNgNodeId'
_I='begemotNgTypeName'
_H='Unsigned32'
_G='not-accessible'
_F='read-write'
_E='31a'
_D='BEGEMOT-NETGRAPH-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
begemot,=mibBuilder.importSymbols('BEGEMOT-MIB','begemot')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
begemotNg=ModuleIdentity((1,3,6,1,4,1,12325,1,2))
if mibBuilder.loadTexts:begemotNg.setRevisions(('2003-11-14 00:00','2002-01-31 00:00'))
class NgTypeName(TextualConvention,OctetString):status=_A;displayHint=_E;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
class NgNodeName(TextualConvention,OctetString):status=_A;displayHint=_E;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
class NgNodeNameOrEmpty(TextualConvention,OctetString):status=_A;displayHint=_E;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
class NgHookName(TextualConvention,OctetString):status=_A;displayHint=_E;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
class NgNodeId(TextualConvention,Unsigned32):status=_A;displayHint='x';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class NgNodeIdOrZero(TextualConvention,Unsigned32):status=_A;displayHint='x';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_BegemotNgObjects_ObjectIdentity=ObjectIdentity
begemotNgObjects=_BegemotNgObjects_ObjectIdentity((1,3,6,1,4,1,12325,1,2,1))
_BegemotNgConfig_ObjectIdentity=ObjectIdentity
begemotNgConfig=_BegemotNgConfig_ObjectIdentity((1,3,6,1,4,1,12325,1,2,1,1))
_BegemotNgControlNodeName_Type=NgNodeName
_BegemotNgControlNodeName_Object=MibScalar
begemotNgControlNodeName=_BegemotNgControlNodeName_Object((1,3,6,1,4,1,12325,1,2,1,1,1),_BegemotNgControlNodeName_Type())
begemotNgControlNodeName.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotNgControlNodeName.setStatus(_A)
class _BegemotNgResBufSiz_Type(Integer32):defaultValue=20000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,65536))
_BegemotNgResBufSiz_Type.__name__=_C
_BegemotNgResBufSiz_Object=MibScalar
begemotNgResBufSiz=_BegemotNgResBufSiz_Object((1,3,6,1,4,1,12325,1,2,1,1,2),_BegemotNgResBufSiz_Type())
begemotNgResBufSiz.setMaxAccess(_F)
if mibBuilder.loadTexts:begemotNgResBufSiz.setStatus(_A)
class _BegemotNgTimeout_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10000))
_BegemotNgTimeout_Type.__name__=_C
_BegemotNgTimeout_Object=MibScalar
begemotNgTimeout=_BegemotNgTimeout_Object((1,3,6,1,4,1,12325,1,2,1,1,3),_BegemotNgTimeout_Type())
begemotNgTimeout.setMaxAccess(_F)
if mibBuilder.loadTexts:begemotNgTimeout.setStatus(_A)
if mibBuilder.loadTexts:begemotNgTimeout.setUnits('milliseconds')
class _BegemotNgDebugLevel_Type(Unsigned32):defaultValue=0
_BegemotNgDebugLevel_Type.__name__=_H
_BegemotNgDebugLevel_Object=MibScalar
begemotNgDebugLevel=_BegemotNgDebugLevel_Object((1,3,6,1,4,1,12325,1,2,1,1,4),_BegemotNgDebugLevel_Type())
begemotNgDebugLevel.setMaxAccess(_F)
if mibBuilder.loadTexts:begemotNgDebugLevel.setStatus(_A)
_BegemotNgStats_ObjectIdentity=ObjectIdentity
begemotNgStats=_BegemotNgStats_ObjectIdentity((1,3,6,1,4,1,12325,1,2,1,2))
_BegemotNgNoMems_Type=Counter32
_BegemotNgNoMems_Object=MibScalar
begemotNgNoMems=_BegemotNgNoMems_Object((1,3,6,1,4,1,12325,1,2,1,2,1),_BegemotNgNoMems_Type())
begemotNgNoMems.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotNgNoMems.setStatus(_A)
_BegemotNgMsgReadErrs_Type=Counter32
_BegemotNgMsgReadErrs_Object=MibScalar
begemotNgMsgReadErrs=_BegemotNgMsgReadErrs_Object((1,3,6,1,4,1,12325,1,2,1,2,2),_BegemotNgMsgReadErrs_Type())
begemotNgMsgReadErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotNgMsgReadErrs.setStatus(_A)
_BegemotNgTooLargeMsgs_Type=Counter32
_BegemotNgTooLargeMsgs_Object=MibScalar
begemotNgTooLargeMsgs=_BegemotNgTooLargeMsgs_Object((1,3,6,1,4,1,12325,1,2,1,2,3),_BegemotNgTooLargeMsgs_Type())
begemotNgTooLargeMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotNgTooLargeMsgs.setStatus(_A)
_BegemotNgDataReadErrs_Type=Counter32
_BegemotNgDataReadErrs_Object=MibScalar
begemotNgDataReadErrs=_BegemotNgDataReadErrs_Object((1,3,6,1,4,1,12325,1,2,1,2,4),_BegemotNgDataReadErrs_Type())
begemotNgDataReadErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotNgDataReadErrs.setStatus(_A)
_BegemotNgTooLargeDatas_Type=Counter32
_BegemotNgTooLargeDatas_Object=MibScalar
begemotNgTooLargeDatas=_BegemotNgTooLargeDatas_Object((1,3,6,1,4,1,12325,1,2,1,2,5),_BegemotNgTooLargeDatas_Type())
begemotNgTooLargeDatas.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotNgTooLargeDatas.setStatus(_A)
_BegemotNgTypeTable_Object=MibTable
begemotNgTypeTable=_BegemotNgTypeTable_Object((1,3,6,1,4,1,12325,1,2,1,3))
if mibBuilder.loadTexts:begemotNgTypeTable.setStatus(_A)
_BegemotNgTypeEntry_Object=MibTableRow
begemotNgTypeEntry=_BegemotNgTypeEntry_Object((1,3,6,1,4,1,12325,1,2,1,3,1))
begemotNgTypeEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:begemotNgTypeEntry.setStatus(_A)
_BegemotNgTypeName_Type=NgTypeName
_BegemotNgTypeName_Object=MibTableColumn
begemotNgTypeName=_BegemotNgTypeName_Object((1,3,6,1,4,1,12325,1,2,1,3,1,1),_BegemotNgTypeName_Type())
begemotNgTypeName.setMaxAccess(_G)
if mibBuilder.loadTexts:begemotNgTypeName.setStatus(_A)
class _BegemotNgTypeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('loaded',1),('unloaded',2)))
_BegemotNgTypeStatus_Type.__name__=_C
_BegemotNgTypeStatus_Object=MibTableColumn
begemotNgTypeStatus=_BegemotNgTypeStatus_Object((1,3,6,1,4,1,12325,1,2,1,3,1,2),_BegemotNgTypeStatus_Type())
begemotNgTypeStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:begemotNgTypeStatus.setStatus(_A)
_BegemotNgNodeTable_Object=MibTable
begemotNgNodeTable=_BegemotNgNodeTable_Object((1,3,6,1,4,1,12325,1,2,1,4))
if mibBuilder.loadTexts:begemotNgNodeTable.setStatus(_A)
_BegemotNgNodeEntry_Object=MibTableRow
begemotNgNodeEntry=_BegemotNgNodeEntry_Object((1,3,6,1,4,1,12325,1,2,1,4,1))
begemotNgNodeEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:begemotNgNodeEntry.setStatus(_A)
_BegemotNgNodeId_Type=NgNodeId
_BegemotNgNodeId_Object=MibTableColumn
begemotNgNodeId=_BegemotNgNodeId_Object((1,3,6,1,4,1,12325,1,2,1,4,1,1),_BegemotNgNodeId_Type())
begemotNgNodeId.setMaxAccess(_G)
if mibBuilder.loadTexts:begemotNgNodeId.setStatus(_A)
class _BegemotNgNodeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_K,2)))
_BegemotNgNodeStatus_Type.__name__=_C
_BegemotNgNodeStatus_Object=MibTableColumn
begemotNgNodeStatus=_BegemotNgNodeStatus_Object((1,3,6,1,4,1,12325,1,2,1,4,1,2),_BegemotNgNodeStatus_Type())
begemotNgNodeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotNgNodeStatus.setStatus(_A)
_BegemotNgNodeName_Type=NgNodeNameOrEmpty
_BegemotNgNodeName_Object=MibTableColumn
begemotNgNodeName=_BegemotNgNodeName_Object((1,3,6,1,4,1,12325,1,2,1,4,1,3),_BegemotNgNodeName_Type())
begemotNgNodeName.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotNgNodeName.setStatus(_A)
_BegemotNgNodeType_Type=NgTypeName
_BegemotNgNodeType_Object=MibTableColumn
begemotNgNodeType=_BegemotNgNodeType_Object((1,3,6,1,4,1,12325,1,2,1,4,1,4),_BegemotNgNodeType_Type())
begemotNgNodeType.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotNgNodeType.setStatus(_A)
_BegemotNgNodeHooks_Type=Unsigned32
_BegemotNgNodeHooks_Object=MibTableColumn
begemotNgNodeHooks=_BegemotNgNodeHooks_Object((1,3,6,1,4,1,12325,1,2,1,4,1,5),_BegemotNgNodeHooks_Type())
begemotNgNodeHooks.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotNgNodeHooks.setStatus(_A)
_BegemotNgHookTable_Object=MibTable
begemotNgHookTable=_BegemotNgHookTable_Object((1,3,6,1,4,1,12325,1,2,1,5))
if mibBuilder.loadTexts:begemotNgHookTable.setStatus(_A)
_BegemotNgHookEntry_Object=MibTableRow
begemotNgHookEntry=_BegemotNgHookEntry_Object((1,3,6,1,4,1,12325,1,2,1,5,1))
begemotNgHookEntry.setIndexNames((0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:begemotNgHookEntry.setStatus(_A)
_BegemotNgHookNodeId_Type=NgNodeId
_BegemotNgHookNodeId_Object=MibTableColumn
begemotNgHookNodeId=_BegemotNgHookNodeId_Object((1,3,6,1,4,1,12325,1,2,1,5,1,1),_BegemotNgHookNodeId_Type())
begemotNgHookNodeId.setMaxAccess(_G)
if mibBuilder.loadTexts:begemotNgHookNodeId.setStatus(_A)
_BegemotNgHookHook_Type=NgHookName
_BegemotNgHookHook_Object=MibTableColumn
begemotNgHookHook=_BegemotNgHookHook_Object((1,3,6,1,4,1,12325,1,2,1,5,1,2),_BegemotNgHookHook_Type())
begemotNgHookHook.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotNgHookHook.setStatus(_A)
class _BegemotNgHookStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_K,2)))
_BegemotNgHookStatus_Type.__name__=_C
_BegemotNgHookStatus_Object=MibTableColumn
begemotNgHookStatus=_BegemotNgHookStatus_Object((1,3,6,1,4,1,12325,1,2,1,5,1,3),_BegemotNgHookStatus_Type())
begemotNgHookStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotNgHookStatus.setStatus(_A)
_BegemotNgHookPeerNodeId_Type=NgNodeId
_BegemotNgHookPeerNodeId_Object=MibTableColumn
begemotNgHookPeerNodeId=_BegemotNgHookPeerNodeId_Object((1,3,6,1,4,1,12325,1,2,1,5,1,4),_BegemotNgHookPeerNodeId_Type())
begemotNgHookPeerNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotNgHookPeerNodeId.setStatus(_A)
_BegemotNgHookPeerHook_Type=NgHookName
_BegemotNgHookPeerHook_Object=MibTableColumn
begemotNgHookPeerHook=_BegemotNgHookPeerHook_Object((1,3,6,1,4,1,12325,1,2,1,5,1,5),_BegemotNgHookPeerHook_Type())
begemotNgHookPeerHook.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotNgHookPeerHook.setStatus(_A)
_BegemotNgHookPeerType_Type=NgTypeName
_BegemotNgHookPeerType_Object=MibTableColumn
begemotNgHookPeerType=_BegemotNgHookPeerType_Object((1,3,6,1,4,1,12325,1,2,1,5,1,6),_BegemotNgHookPeerType_Type())
begemotNgHookPeerType.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotNgHookPeerType.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'NgTypeName':NgTypeName,'NgNodeName':NgNodeName,'NgNodeNameOrEmpty':NgNodeNameOrEmpty,'NgHookName':NgHookName,'NgNodeId':NgNodeId,'NgNodeIdOrZero':NgNodeIdOrZero,'begemotNg':begemotNg,'begemotNgObjects':begemotNgObjects,'begemotNgConfig':begemotNgConfig,'begemotNgControlNodeName':begemotNgControlNodeName,'begemotNgResBufSiz':begemotNgResBufSiz,'begemotNgTimeout':begemotNgTimeout,'begemotNgDebugLevel':begemotNgDebugLevel,'begemotNgStats':begemotNgStats,'begemotNgNoMems':begemotNgNoMems,'begemotNgMsgReadErrs':begemotNgMsgReadErrs,'begemotNgTooLargeMsgs':begemotNgTooLargeMsgs,'begemotNgDataReadErrs':begemotNgDataReadErrs,'begemotNgTooLargeDatas':begemotNgTooLargeDatas,'begemotNgTypeTable':begemotNgTypeTable,'begemotNgTypeEntry':begemotNgTypeEntry,_I:begemotNgTypeName,'begemotNgTypeStatus':begemotNgTypeStatus,'begemotNgNodeTable':begemotNgNodeTable,'begemotNgNodeEntry':begemotNgNodeEntry,_J:begemotNgNodeId,'begemotNgNodeStatus':begemotNgNodeStatus,'begemotNgNodeName':begemotNgNodeName,'begemotNgNodeType':begemotNgNodeType,'begemotNgNodeHooks':begemotNgNodeHooks,'begemotNgHookTable':begemotNgHookTable,'begemotNgHookEntry':begemotNgHookEntry,_L:begemotNgHookNodeId,_M:begemotNgHookHook,'begemotNgHookStatus':begemotNgHookStatus,'begemotNgHookPeerNodeId':begemotNgHookPeerNodeId,'begemotNgHookPeerHook':begemotNgHookPeerHook,'begemotNgHookPeerType':begemotNgHookPeerType})