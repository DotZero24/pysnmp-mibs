_X='swVlanTranslationCVID'
_W='swQinQRuleAccessID'
_V='swQinQRuleProfileID'
_U='swQinQProfileID'
_T='swDoubleVlanTranslateCVID'
_S='swDoubleVlanTranslateSVID'
_R='swDoubleVlanTranslatePortIndex'
_Q='swVlanTranslateCVID'
_P='swVlanTranslatePortIndex'
_O='swQinQProfileId'
_N='swQinQPortRuleIndex'
_M='swQinQPortIndex'
_L='not-accessible'
_K='add'
_J='replace'
_I='OctetString'
_H='disabled'
_G='enabled'
_F='read-only'
_E='read-write'
_D='Q-IN-Q-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
swQinQMIB=ModuleIdentity((1,3,6,1,4,1,171,12,57))
class VlanId(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwQinQCtrl_ObjectIdentity=ObjectIdentity
swQinQCtrl=_SwQinQCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,57,1))
class _SwQinQState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwQinQState_Type.__name__=_C
_SwQinQState_Object=MibScalar
swQinQState=_SwQinQState_Object((1,3,6,1,4,1,171,12,57,1,1),_SwQinQState_Type())
swQinQState.setMaxAccess(_E)
if mibBuilder.loadTexts:swQinQState.setStatus(_A)
class _SwQinQInnerTpid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_SwQinQInnerTpid_Type.__name__=_I
_SwQinQInnerTpid_Object=MibScalar
swQinQInnerTpid=_SwQinQInnerTpid_Object((1,3,6,1,4,1,171,12,57,1,2),_SwQinQInnerTpid_Type())
swQinQInnerTpid.setMaxAccess(_E)
if mibBuilder.loadTexts:swQinQInnerTpid.setStatus(_A)
_SwQinQInfo_ObjectIdentity=ObjectIdentity
swQinQInfo=_SwQinQInfo_ObjectIdentity((1,3,6,1,4,1,171,12,57,2))
_SwQinQPortMgmt_ObjectIdentity=ObjectIdentity
swQinQPortMgmt=_SwQinQPortMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,57,3))
_SwQinQPortTable_Object=MibTable
swQinQPortTable=_SwQinQPortTable_Object((1,3,6,1,4,1,171,12,57,3,1))
if mibBuilder.loadTexts:swQinQPortTable.setStatus(_A)
_SwQinQPortEntry_Object=MibTableRow
swQinQPortEntry=_SwQinQPortEntry_Object((1,3,6,1,4,1,171,12,57,3,1,1))
swQinQPortEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:swQinQPortEntry.setStatus(_A)
class _SwQinQPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwQinQPortIndex_Type.__name__=_C
_SwQinQPortIndex_Object=MibTableColumn
swQinQPortIndex=_SwQinQPortIndex_Object((1,3,6,1,4,1,171,12,57,3,1,1,1),_SwQinQPortIndex_Type())
swQinQPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:swQinQPortIndex.setStatus(_A)
class _SwQinQPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nni',1),('uni',2)))
_SwQinQPortRole_Type.__name__=_C
_SwQinQPortRole_Object=MibTableColumn
swQinQPortRole=_SwQinQPortRole_Object((1,3,6,1,4,1,171,12,57,3,1,1,2),_SwQinQPortRole_Type())
swQinQPortRole.setMaxAccess(_E)
if mibBuilder.loadTexts:swQinQPortRole.setStatus(_A)
class _SwQinQPortMissDrop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwQinQPortMissDrop_Type.__name__=_C
_SwQinQPortMissDrop_Object=MibTableColumn
swQinQPortMissDrop=_SwQinQPortMissDrop_Object((1,3,6,1,4,1,171,12,57,3,1,1,3),_SwQinQPortMissDrop_Type())
swQinQPortMissDrop.setMaxAccess(_E)
if mibBuilder.loadTexts:swQinQPortMissDrop.setStatus(_A)
class _SwQinQPortTpid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_SwQinQPortTpid_Type.__name__=_I
_SwQinQPortTpid_Object=MibTableColumn
swQinQPortTpid=_SwQinQPortTpid_Object((1,3,6,1,4,1,171,12,57,3,1,1,4),_SwQinQPortTpid_Type())
swQinQPortTpid.setMaxAccess(_E)
if mibBuilder.loadTexts:swQinQPortTpid.setStatus(_A)
class _SwQinQPortUseInnerPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwQinQPortUseInnerPriority_Type.__name__=_C
_SwQinQPortUseInnerPriority_Object=MibTableColumn
swQinQPortUseInnerPriority=_SwQinQPortUseInnerPriority_Object((1,3,6,1,4,1,171,12,57,3,1,1,5),_SwQinQPortUseInnerPriority_Type())
swQinQPortUseInnerPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:swQinQPortUseInnerPriority.setStatus(_A)
class _SwQinQPortInnerTagState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwQinQPortInnerTagState_Type.__name__=_C
_SwQinQPortInnerTagState_Object=MibTableColumn
swQinQPortInnerTagState=_SwQinQPortInnerTagState_Object((1,3,6,1,4,1,171,12,57,3,1,1,6),_SwQinQPortInnerTagState_Type())
swQinQPortInnerTagState.setMaxAccess(_E)
if mibBuilder.loadTexts:swQinQPortInnerTagState.setStatus(_A)
class _SwQinQPortInnerTag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_SwQinQPortInnerTag_Type.__name__=_I
_SwQinQPortInnerTag_Object=MibTableColumn
swQinQPortInnerTag=_SwQinQPortInnerTag_Object((1,3,6,1,4,1,171,12,57,3,1,1,7),_SwQinQPortInnerTag_Type())
swQinQPortInnerTag.setMaxAccess(_E)
if mibBuilder.loadTexts:swQinQPortInnerTag.setStatus(_A)
class _SwQinQPortTrustCVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwQinQPortTrustCVID_Type.__name__=_C
_SwQinQPortTrustCVID_Object=MibTableColumn
swQinQPortTrustCVID=_SwQinQPortTrustCVID_Object((1,3,6,1,4,1,171,12,57,3,1,1,8),_SwQinQPortTrustCVID_Type())
swQinQPortTrustCVID.setMaxAccess(_E)
if mibBuilder.loadTexts:swQinQPortTrustCVID.setStatus(_A)
class _SwQinQPortVlanTranslation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwQinQPortVlanTranslation_Type.__name__=_C
_SwQinQPortVlanTranslation_Object=MibTableColumn
swQinQPortVlanTranslation=_SwQinQPortVlanTranslation_Object((1,3,6,1,4,1,171,12,57,3,1,1,9),_SwQinQPortVlanTranslation_Type())
swQinQPortVlanTranslation.setMaxAccess(_E)
if mibBuilder.loadTexts:swQinQPortVlanTranslation.setStatus(_A)
class _SwQinQPortInnerTpid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_SwQinQPortInnerTpid_Type.__name__=_I
_SwQinQPortInnerTpid_Object=MibTableColumn
swQinQPortInnerTpid=_SwQinQPortInnerTpid_Object((1,3,6,1,4,1,171,12,57,3,1,1,10),_SwQinQPortInnerTpid_Type())
swQinQPortInnerTpid.setMaxAccess(_E)
if mibBuilder.loadTexts:swQinQPortInnerTpid.setStatus(_A)
_SwQinQPortRuleTable_Object=MibTable
swQinQPortRuleTable=_SwQinQPortRuleTable_Object((1,3,6,1,4,1,171,12,57,3,2))
if mibBuilder.loadTexts:swQinQPortRuleTable.setStatus(_A)
_SwQinQPortRuleEntry_Object=MibTableRow
swQinQPortRuleEntry=_SwQinQPortRuleEntry_Object((1,3,6,1,4,1,171,12,57,3,2,1))
swQinQPortRuleEntry.setIndexNames((0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:swQinQPortRuleEntry.setStatus(_A)
class _SwQinQPortRuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwQinQPortRuleIndex_Type.__name__=_C
_SwQinQPortRuleIndex_Object=MibTableColumn
swQinQPortRuleIndex=_SwQinQPortRuleIndex_Object((1,3,6,1,4,1,171,12,57,3,2,1,1),_SwQinQPortRuleIndex_Type())
swQinQPortRuleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:swQinQPortRuleIndex.setStatus(_A)
class _SwQinQProfileId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwQinQProfileId_Type.__name__=_C
_SwQinQProfileId_Object=MibTableColumn
swQinQProfileId=_SwQinQProfileId_Object((1,3,6,1,4,1,171,12,57,3,2,1,2),_SwQinQProfileId_Type())
swQinQProfileId.setMaxAccess(_F)
if mibBuilder.loadTexts:swQinQProfileId.setStatus(_A)
_SwQinQPortRuleRowStatus_Type=RowStatus
_SwQinQPortRuleRowStatus_Object=MibTableColumn
swQinQPortRuleRowStatus=_SwQinQPortRuleRowStatus_Object((1,3,6,1,4,1,171,12,57,3,2,1,3),_SwQinQPortRuleRowStatus_Type())
swQinQPortRuleRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swQinQPortRuleRowStatus.setStatus(_A)
_SwVlanTranslateTable_Object=MibTable
swVlanTranslateTable=_SwVlanTranslateTable_Object((1,3,6,1,4,1,171,12,57,3,3))
if mibBuilder.loadTexts:swVlanTranslateTable.setStatus(_A)
_SwVlanTranslateEntry_Object=MibTableRow
swVlanTranslateEntry=_SwVlanTranslateEntry_Object((1,3,6,1,4,1,171,12,57,3,3,1))
swVlanTranslateEntry.setIndexNames((0,_D,_P),(0,_D,_Q))
if mibBuilder.loadTexts:swVlanTranslateEntry.setStatus(_A)
_SwVlanTranslatePortIndex_Type=Integer32
_SwVlanTranslatePortIndex_Object=MibTableColumn
swVlanTranslatePortIndex=_SwVlanTranslatePortIndex_Object((1,3,6,1,4,1,171,12,57,3,3,1,1),_SwVlanTranslatePortIndex_Type())
swVlanTranslatePortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:swVlanTranslatePortIndex.setStatus(_A)
_SwVlanTranslateCVID_Type=VlanId
_SwVlanTranslateCVID_Object=MibTableColumn
swVlanTranslateCVID=_SwVlanTranslateCVID_Object((1,3,6,1,4,1,171,12,57,3,3,1,2),_SwVlanTranslateCVID_Type())
swVlanTranslateCVID.setMaxAccess(_F)
if mibBuilder.loadTexts:swVlanTranslateCVID.setStatus(_A)
_SwVlanTranslateSVID_Type=VlanId
_SwVlanTranslateSVID_Object=MibTableColumn
swVlanTranslateSVID=_SwVlanTranslateSVID_Object((1,3,6,1,4,1,171,12,57,3,3,1,3),_SwVlanTranslateSVID_Type())
swVlanTranslateSVID.setMaxAccess(_B)
if mibBuilder.loadTexts:swVlanTranslateSVID.setStatus(_A)
class _SwVlanTranslateSVIDOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_SwVlanTranslateSVIDOperation_Type.__name__=_C
_SwVlanTranslateSVIDOperation_Object=MibTableColumn
swVlanTranslateSVIDOperation=_SwVlanTranslateSVIDOperation_Object((1,3,6,1,4,1,171,12,57,3,3,1,4),_SwVlanTranslateSVIDOperation_Type())
swVlanTranslateSVIDOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:swVlanTranslateSVIDOperation.setStatus(_A)
class _SwVlanTranslatePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,7))
_SwVlanTranslatePriority_Type.__name__=_C
_SwVlanTranslatePriority_Object=MibTableColumn
swVlanTranslatePriority=_SwVlanTranslatePriority_Object((1,3,6,1,4,1,171,12,57,3,3,1,5),_SwVlanTranslatePriority_Type())
swVlanTranslatePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:swVlanTranslatePriority.setStatus(_A)
_SwVlanTranslateRowStatus_Type=RowStatus
_SwVlanTranslateRowStatus_Object=MibTableColumn
swVlanTranslateRowStatus=_SwVlanTranslateRowStatus_Object((1,3,6,1,4,1,171,12,57,3,3,1,6),_SwVlanTranslateRowStatus_Type())
swVlanTranslateRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swVlanTranslateRowStatus.setStatus(_A)
_SwDoubleVlanTranslateTable_Object=MibTable
swDoubleVlanTranslateTable=_SwDoubleVlanTranslateTable_Object((1,3,6,1,4,1,171,12,57,3,4))
if mibBuilder.loadTexts:swDoubleVlanTranslateTable.setStatus(_A)
_SwDoubleVlanTranslateEntry_Object=MibTableRow
swDoubleVlanTranslateEntry=_SwDoubleVlanTranslateEntry_Object((1,3,6,1,4,1,171,12,57,3,4,1))
swDoubleVlanTranslateEntry.setIndexNames((0,_D,_R),(0,_D,_S),(0,_D,_T))
if mibBuilder.loadTexts:swDoubleVlanTranslateEntry.setStatus(_A)
_SwDoubleVlanTranslatePortIndex_Type=Integer32
_SwDoubleVlanTranslatePortIndex_Object=MibTableColumn
swDoubleVlanTranslatePortIndex=_SwDoubleVlanTranslatePortIndex_Object((1,3,6,1,4,1,171,12,57,3,4,1,1),_SwDoubleVlanTranslatePortIndex_Type())
swDoubleVlanTranslatePortIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:swDoubleVlanTranslatePortIndex.setStatus(_A)
_SwDoubleVlanTranslateSVID_Type=VlanId
_SwDoubleVlanTranslateSVID_Object=MibTableColumn
swDoubleVlanTranslateSVID=_SwDoubleVlanTranslateSVID_Object((1,3,6,1,4,1,171,12,57,3,4,1,2),_SwDoubleVlanTranslateSVID_Type())
swDoubleVlanTranslateSVID.setMaxAccess(_L)
if mibBuilder.loadTexts:swDoubleVlanTranslateSVID.setStatus(_A)
_SwDoubleVlanTranslateCVID_Type=VlanId
_SwDoubleVlanTranslateCVID_Object=MibTableColumn
swDoubleVlanTranslateCVID=_SwDoubleVlanTranslateCVID_Object((1,3,6,1,4,1,171,12,57,3,4,1,3),_SwDoubleVlanTranslateCVID_Type())
swDoubleVlanTranslateCVID.setMaxAccess(_L)
if mibBuilder.loadTexts:swDoubleVlanTranslateCVID.setStatus(_A)
class _SwDoubleVlanTranslateOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues((_J,2))
_SwDoubleVlanTranslateOperation_Type.__name__=_C
_SwDoubleVlanTranslateOperation_Object=MibTableColumn
swDoubleVlanTranslateOperation=_SwDoubleVlanTranslateOperation_Object((1,3,6,1,4,1,171,12,57,3,4,1,4),_SwDoubleVlanTranslateOperation_Type())
swDoubleVlanTranslateOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:swDoubleVlanTranslateOperation.setStatus(_A)
_SwDoubleVlanTranslateNewSVID_Type=VlanId
_SwDoubleVlanTranslateNewSVID_Object=MibTableColumn
swDoubleVlanTranslateNewSVID=_SwDoubleVlanTranslateNewSVID_Object((1,3,6,1,4,1,171,12,57,3,4,1,5),_SwDoubleVlanTranslateNewSVID_Type())
swDoubleVlanTranslateNewSVID.setMaxAccess(_B)
if mibBuilder.loadTexts:swDoubleVlanTranslateNewSVID.setStatus(_A)
class _SwDoubleVlanTranslatePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,7))
_SwDoubleVlanTranslatePriority_Type.__name__=_C
_SwDoubleVlanTranslatePriority_Object=MibTableColumn
swDoubleVlanTranslatePriority=_SwDoubleVlanTranslatePriority_Object((1,3,6,1,4,1,171,12,57,3,4,1,6),_SwDoubleVlanTranslatePriority_Type())
swDoubleVlanTranslatePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:swDoubleVlanTranslatePriority.setStatus(_A)
_SwDoubleVlanTranslateRowStatus_Type=RowStatus
_SwDoubleVlanTranslateRowStatus_Object=MibTableColumn
swDoubleVlanTranslateRowStatus=_SwDoubleVlanTranslateRowStatus_Object((1,3,6,1,4,1,171,12,57,3,4,1,7),_SwDoubleVlanTranslateRowStatus_Type())
swDoubleVlanTranslateRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swDoubleVlanTranslateRowStatus.setStatus(_A)
_SwQinQMgmt_ObjectIdentity=ObjectIdentity
swQinQMgmt=_SwQinQMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,57,4))
_SwQinQProfileTable_Object=MibTable
swQinQProfileTable=_SwQinQProfileTable_Object((1,3,6,1,4,1,171,12,57,4,1))
if mibBuilder.loadTexts:swQinQProfileTable.setStatus(_A)
_SwQinQProfileEntry_Object=MibTableRow
swQinQProfileEntry=_SwQinQProfileEntry_Object((1,3,6,1,4,1,171,12,57,4,1,1))
swQinQProfileEntry.setIndexNames((0,_D,_U))
if mibBuilder.loadTexts:swQinQProfileEntry.setStatus(_A)
class _SwQinQProfileID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwQinQProfileID_Type.__name__=_C
_SwQinQProfileID_Object=MibTableColumn
swQinQProfileID=_SwQinQProfileID_Object((1,3,6,1,4,1,171,12,57,4,1,1,1),_SwQinQProfileID_Type())
swQinQProfileID.setMaxAccess(_F)
if mibBuilder.loadTexts:swQinQProfileID.setStatus(_A)
_SwQinQProfileRowStatus_Type=RowStatus
_SwQinQProfileRowStatus_Object=MibTableColumn
swQinQProfileRowStatus=_SwQinQProfileRowStatus_Object((1,3,6,1,4,1,171,12,57,4,1,1,2),_SwQinQProfileRowStatus_Type())
swQinQProfileRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swQinQProfileRowStatus.setStatus(_A)
_SwQinQRuleTable_Object=MibTable
swQinQRuleTable=_SwQinQRuleTable_Object((1,3,6,1,4,1,171,12,57,4,2))
if mibBuilder.loadTexts:swQinQRuleTable.setStatus(_A)
_SwQinQRuleEntry_Object=MibTableRow
swQinQRuleEntry=_SwQinQRuleEntry_Object((1,3,6,1,4,1,171,12,57,4,2,1))
swQinQRuleEntry.setIndexNames((0,_D,_V),(0,_D,_W))
if mibBuilder.loadTexts:swQinQRuleEntry.setStatus(_A)
class _SwQinQRuleProfileID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwQinQRuleProfileID_Type.__name__=_C
_SwQinQRuleProfileID_Object=MibTableColumn
swQinQRuleProfileID=_SwQinQRuleProfileID_Object((1,3,6,1,4,1,171,12,57,4,2,1,1),_SwQinQRuleProfileID_Type())
swQinQRuleProfileID.setMaxAccess(_F)
if mibBuilder.loadTexts:swQinQRuleProfileID.setStatus(_A)
class _SwQinQRuleAccessID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwQinQRuleAccessID_Type.__name__=_C
_SwQinQRuleAccessID_Object=MibTableColumn
swQinQRuleAccessID=_SwQinQRuleAccessID_Object((1,3,6,1,4,1,171,12,57,4,2,1,2),_SwQinQRuleAccessID_Type())
swQinQRuleAccessID.setMaxAccess(_F)
if mibBuilder.loadTexts:swQinQRuleAccessID.setStatus(_A)
_SwQinQRuleClassifySrcMacAddr_Type=MacAddress
_SwQinQRuleClassifySrcMacAddr_Object=MibTableColumn
swQinQRuleClassifySrcMacAddr=_SwQinQRuleClassifySrcMacAddr_Object((1,3,6,1,4,1,171,12,57,4,2,1,3),_SwQinQRuleClassifySrcMacAddr_Type())
swQinQRuleClassifySrcMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swQinQRuleClassifySrcMacAddr.setStatus(_A)
_SwQinQRuleClassifySrcMacAddrMask_Type=MacAddress
_SwQinQRuleClassifySrcMacAddrMask_Object=MibTableColumn
swQinQRuleClassifySrcMacAddrMask=_SwQinQRuleClassifySrcMacAddrMask_Object((1,3,6,1,4,1,171,12,57,4,2,1,4),_SwQinQRuleClassifySrcMacAddrMask_Type())
swQinQRuleClassifySrcMacAddrMask.setMaxAccess(_B)
if mibBuilder.loadTexts:swQinQRuleClassifySrcMacAddrMask.setStatus(_A)
_SwQinQRuleClassifyDstMacAddr_Type=MacAddress
_SwQinQRuleClassifyDstMacAddr_Object=MibTableColumn
swQinQRuleClassifyDstMacAddr=_SwQinQRuleClassifyDstMacAddr_Object((1,3,6,1,4,1,171,12,57,4,2,1,5),_SwQinQRuleClassifyDstMacAddr_Type())
swQinQRuleClassifyDstMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swQinQRuleClassifyDstMacAddr.setStatus(_A)
_SwQinQRuleClassifyDstMacAddrMask_Type=MacAddress
_SwQinQRuleClassifyDstMacAddrMask_Object=MibTableColumn
swQinQRuleClassifyDstMacAddrMask=_SwQinQRuleClassifyDstMacAddrMask_Object((1,3,6,1,4,1,171,12,57,4,2,1,6),_SwQinQRuleClassifyDstMacAddrMask_Type())
swQinQRuleClassifyDstMacAddrMask.setMaxAccess(_B)
if mibBuilder.loadTexts:swQinQRuleClassifyDstMacAddrMask.setStatus(_A)
_SwQinQRuleSrcIPv4Address_Type=IpAddress
_SwQinQRuleSrcIPv4Address_Object=MibTableColumn
swQinQRuleSrcIPv4Address=_SwQinQRuleSrcIPv4Address_Object((1,3,6,1,4,1,171,12,57,4,2,1,7),_SwQinQRuleSrcIPv4Address_Type())
swQinQRuleSrcIPv4Address.setMaxAccess(_B)
if mibBuilder.loadTexts:swQinQRuleSrcIPv4Address.setStatus(_A)
_SwQinQRuleSrcIPv4AddrMask_Type=IpAddress
_SwQinQRuleSrcIPv4AddrMask_Object=MibTableColumn
swQinQRuleSrcIPv4AddrMask=_SwQinQRuleSrcIPv4AddrMask_Object((1,3,6,1,4,1,171,12,57,4,2,1,8),_SwQinQRuleSrcIPv4AddrMask_Type())
swQinQRuleSrcIPv4AddrMask.setMaxAccess(_B)
if mibBuilder.loadTexts:swQinQRuleSrcIPv4AddrMask.setStatus(_A)
_SwQinQRuleDstIPv4Address_Type=IpAddress
_SwQinQRuleDstIPv4Address_Object=MibTableColumn
swQinQRuleDstIPv4Address=_SwQinQRuleDstIPv4Address_Object((1,3,6,1,4,1,171,12,57,4,2,1,9),_SwQinQRuleDstIPv4Address_Type())
swQinQRuleDstIPv4Address.setMaxAccess(_B)
if mibBuilder.loadTexts:swQinQRuleDstIPv4Address.setStatus(_A)
_SwQinQRuleDstIPv4AddrMask_Type=IpAddress
_SwQinQRuleDstIPv4AddrMask_Object=MibTableColumn
swQinQRuleDstIPv4AddrMask=_SwQinQRuleDstIPv4AddrMask_Object((1,3,6,1,4,1,171,12,57,4,2,1,10),_SwQinQRuleDstIPv4AddrMask_Type())
swQinQRuleDstIPv4AddrMask.setMaxAccess(_B)
if mibBuilder.loadTexts:swQinQRuleDstIPv4AddrMask.setStatus(_A)
_SwQinQRuleInnerVid_Type=DisplayString
_SwQinQRuleInnerVid_Object=MibTableColumn
swQinQRuleInnerVid=_SwQinQRuleInnerVid_Object((1,3,6,1,4,1,171,12,57,4,2,1,11),_SwQinQRuleInnerVid_Type())
swQinQRuleInnerVid.setMaxAccess(_B)
if mibBuilder.loadTexts:swQinQRuleInnerVid.setStatus(_A)
_SwQinQRuleOuterVid_Type=DisplayString
_SwQinQRuleOuterVid_Object=MibTableColumn
swQinQRuleOuterVid=_SwQinQRuleOuterVid_Object((1,3,6,1,4,1,171,12,57,4,2,1,12),_SwQinQRuleOuterVid_Type())
swQinQRuleOuterVid.setMaxAccess(_B)
if mibBuilder.loadTexts:swQinQRuleOuterVid.setStatus(_A)
class _SwQinQRule8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,7))
_SwQinQRule8021p_Type.__name__=_C
_SwQinQRule8021p_Object=MibTableColumn
swQinQRule8021p=_SwQinQRule8021p_Object((1,3,6,1,4,1,171,12,57,4,2,1,13),_SwQinQRule8021p_Type())
swQinQRule8021p.setMaxAccess(_B)
if mibBuilder.loadTexts:swQinQRule8021p.setStatus(_A)
_SwQinQRuleIpProtocol_Type=Integer32
_SwQinQRuleIpProtocol_Object=MibTableColumn
swQinQRuleIpProtocol=_SwQinQRuleIpProtocol_Object((1,3,6,1,4,1,171,12,57,4,2,1,14),_SwQinQRuleIpProtocol_Type())
swQinQRuleIpProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:swQinQRuleIpProtocol.setStatus(_A)
_SwQinQRuleSourcePort_Type=Integer32
_SwQinQRuleSourcePort_Object=MibTableColumn
swQinQRuleSourcePort=_SwQinQRuleSourcePort_Object((1,3,6,1,4,1,171,12,57,4,2,1,15),_SwQinQRuleSourcePort_Type())
swQinQRuleSourcePort.setMaxAccess(_B)
if mibBuilder.loadTexts:swQinQRuleSourcePort.setStatus(_A)
_SwQinQRuleDestinationPort_Type=Integer32
_SwQinQRuleDestinationPort_Object=MibTableColumn
swQinQRuleDestinationPort=_SwQinQRuleDestinationPort_Object((1,3,6,1,4,1,171,12,57,4,2,1,16),_SwQinQRuleDestinationPort_Type())
swQinQRuleDestinationPort.setMaxAccess(_B)
if mibBuilder.loadTexts:swQinQRuleDestinationPort.setStatus(_A)
class _SwQinQRuleSpvidOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_SwQinQRuleSpvidOperation_Type.__name__=_C
_SwQinQRuleSpvidOperation_Object=MibTableColumn
swQinQRuleSpvidOperation=_SwQinQRuleSpvidOperation_Object((1,3,6,1,4,1,171,12,57,4,2,1,17),_SwQinQRuleSpvidOperation_Type())
swQinQRuleSpvidOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:swQinQRuleSpvidOperation.setStatus(_A)
class _SwQinQRuleSpvid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwQinQRuleSpvid_Type.__name__=_C
_SwQinQRuleSpvid_Object=MibTableColumn
swQinQRuleSpvid=_SwQinQRuleSpvid_Object((1,3,6,1,4,1,171,12,57,4,2,1,18),_SwQinQRuleSpvid_Type())
swQinQRuleSpvid.setMaxAccess(_B)
if mibBuilder.loadTexts:swQinQRuleSpvid.setStatus(_A)
class _SwQinQPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,7))
_SwQinQPriority_Type.__name__=_C
_SwQinQPriority_Object=MibTableColumn
swQinQPriority=_SwQinQPriority_Object((1,3,6,1,4,1,171,12,57,4,2,1,19),_SwQinQPriority_Type())
swQinQPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:swQinQPriority.setStatus(_A)
_SwQinQRuleRowStatus_Type=RowStatus
_SwQinQRuleRowStatus_Object=MibTableColumn
swQinQRuleRowStatus=_SwQinQRuleRowStatus_Object((1,3,6,1,4,1,171,12,57,4,2,1,20),_SwQinQRuleRowStatus_Type())
swQinQRuleRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swQinQRuleRowStatus.setStatus(_A)
_SwQinQRuleActivePort_Type=PortList
_SwQinQRuleActivePort_Object=MibTableColumn
swQinQRuleActivePort=_SwQinQRuleActivePort_Object((1,3,6,1,4,1,171,12,57,4,2,1,21),_SwQinQRuleActivePort_Type())
swQinQRuleActivePort.setMaxAccess(_F)
if mibBuilder.loadTexts:swQinQRuleActivePort.setStatus(_A)
_SwVlanTranslationCVIDTable_Object=MibTable
swVlanTranslationCVIDTable=_SwVlanTranslationCVIDTable_Object((1,3,6,1,4,1,171,12,57,4,3))
if mibBuilder.loadTexts:swVlanTranslationCVIDTable.setStatus(_A)
_SwVlanTranslationCVIDEntry_Object=MibTableRow
swVlanTranslationCVIDEntry=_SwVlanTranslationCVIDEntry_Object((1,3,6,1,4,1,171,12,57,4,3,1))
swVlanTranslationCVIDEntry.setIndexNames((0,_D,_X))
if mibBuilder.loadTexts:swVlanTranslationCVIDEntry.setStatus(_A)
_SwVlanTranslationCVID_Type=VlanId
_SwVlanTranslationCVID_Object=MibTableColumn
swVlanTranslationCVID=_SwVlanTranslationCVID_Object((1,3,6,1,4,1,171,12,57,4,3,1,1),_SwVlanTranslationCVID_Type())
swVlanTranslationCVID.setMaxAccess(_F)
if mibBuilder.loadTexts:swVlanTranslationCVID.setStatus(_A)
_SwVlanTranslationSVID_Type=VlanId
_SwVlanTranslationSVID_Object=MibTableColumn
swVlanTranslationSVID=_SwVlanTranslationSVID_Object((1,3,6,1,4,1,171,12,57,4,3,1,2),_SwVlanTranslationSVID_Type())
swVlanTranslationSVID.setMaxAccess(_B)
if mibBuilder.loadTexts:swVlanTranslationSVID.setStatus(_A)
class _SwVlanTranslationSVIDOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_SwVlanTranslationSVIDOperation_Type.__name__=_C
_SwVlanTranslationSVIDOperation_Object=MibTableColumn
swVlanTranslationSVIDOperation=_SwVlanTranslationSVIDOperation_Object((1,3,6,1,4,1,171,12,57,4,3,1,3),_SwVlanTranslationSVIDOperation_Type())
swVlanTranslationSVIDOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:swVlanTranslationSVIDOperation.setStatus(_A)
_SwVlanTranslationCVIDRowStatus_Type=RowStatus
_SwVlanTranslationCVIDRowStatus_Object=MibTableColumn
swVlanTranslationCVIDRowStatus=_SwVlanTranslationCVIDRowStatus_Object((1,3,6,1,4,1,171,12,57,4,3,1,4),_SwVlanTranslationCVIDRowStatus_Type())
swVlanTranslationCVIDRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swVlanTranslationCVIDRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'VlanId':VlanId,'swQinQMIB':swQinQMIB,'swQinQCtrl':swQinQCtrl,'swQinQState':swQinQState,'swQinQInnerTpid':swQinQInnerTpid,'swQinQInfo':swQinQInfo,'swQinQPortMgmt':swQinQPortMgmt,'swQinQPortTable':swQinQPortTable,'swQinQPortEntry':swQinQPortEntry,_M:swQinQPortIndex,'swQinQPortRole':swQinQPortRole,'swQinQPortMissDrop':swQinQPortMissDrop,'swQinQPortTpid':swQinQPortTpid,'swQinQPortUseInnerPriority':swQinQPortUseInnerPriority,'swQinQPortInnerTagState':swQinQPortInnerTagState,'swQinQPortInnerTag':swQinQPortInnerTag,'swQinQPortTrustCVID':swQinQPortTrustCVID,'swQinQPortVlanTranslation':swQinQPortVlanTranslation,'swQinQPortInnerTpid':swQinQPortInnerTpid,'swQinQPortRuleTable':swQinQPortRuleTable,'swQinQPortRuleEntry':swQinQPortRuleEntry,_N:swQinQPortRuleIndex,_O:swQinQProfileId,'swQinQPortRuleRowStatus':swQinQPortRuleRowStatus,'swVlanTranslateTable':swVlanTranslateTable,'swVlanTranslateEntry':swVlanTranslateEntry,_P:swVlanTranslatePortIndex,_Q:swVlanTranslateCVID,'swVlanTranslateSVID':swVlanTranslateSVID,'swVlanTranslateSVIDOperation':swVlanTranslateSVIDOperation,'swVlanTranslatePriority':swVlanTranslatePriority,'swVlanTranslateRowStatus':swVlanTranslateRowStatus,'swDoubleVlanTranslateTable':swDoubleVlanTranslateTable,'swDoubleVlanTranslateEntry':swDoubleVlanTranslateEntry,_R:swDoubleVlanTranslatePortIndex,_S:swDoubleVlanTranslateSVID,_T:swDoubleVlanTranslateCVID,'swDoubleVlanTranslateOperation':swDoubleVlanTranslateOperation,'swDoubleVlanTranslateNewSVID':swDoubleVlanTranslateNewSVID,'swDoubleVlanTranslatePriority':swDoubleVlanTranslatePriority,'swDoubleVlanTranslateRowStatus':swDoubleVlanTranslateRowStatus,'swQinQMgmt':swQinQMgmt,'swQinQProfileTable':swQinQProfileTable,'swQinQProfileEntry':swQinQProfileEntry,_U:swQinQProfileID,'swQinQProfileRowStatus':swQinQProfileRowStatus,'swQinQRuleTable':swQinQRuleTable,'swQinQRuleEntry':swQinQRuleEntry,_V:swQinQRuleProfileID,_W:swQinQRuleAccessID,'swQinQRuleClassifySrcMacAddr':swQinQRuleClassifySrcMacAddr,'swQinQRuleClassifySrcMacAddrMask':swQinQRuleClassifySrcMacAddrMask,'swQinQRuleClassifyDstMacAddr':swQinQRuleClassifyDstMacAddr,'swQinQRuleClassifyDstMacAddrMask':swQinQRuleClassifyDstMacAddrMask,'swQinQRuleSrcIPv4Address':swQinQRuleSrcIPv4Address,'swQinQRuleSrcIPv4AddrMask':swQinQRuleSrcIPv4AddrMask,'swQinQRuleDstIPv4Address':swQinQRuleDstIPv4Address,'swQinQRuleDstIPv4AddrMask':swQinQRuleDstIPv4AddrMask,'swQinQRuleInnerVid':swQinQRuleInnerVid,'swQinQRuleOuterVid':swQinQRuleOuterVid,'swQinQRule8021p':swQinQRule8021p,'swQinQRuleIpProtocol':swQinQRuleIpProtocol,'swQinQRuleSourcePort':swQinQRuleSourcePort,'swQinQRuleDestinationPort':swQinQRuleDestinationPort,'swQinQRuleSpvidOperation':swQinQRuleSpvidOperation,'swQinQRuleSpvid':swQinQRuleSpvid,'swQinQPriority':swQinQPriority,'swQinQRuleRowStatus':swQinQRuleRowStatus,'swQinQRuleActivePort':swQinQRuleActivePort,'swVlanTranslationCVIDTable':swVlanTranslationCVIDTable,'swVlanTranslationCVIDEntry':swVlanTranslationCVIDEntry,_X:swVlanTranslationCVID,'swVlanTranslationSVID':swVlanTranslationSVID,'swVlanTranslationSVIDOperation':swVlanTranslationSVIDOperation,'swVlanTranslationCVIDRowStatus':swVlanTranslationCVIDRowStatus})