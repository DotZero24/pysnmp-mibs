_L='h3cRrppPortID'
_K='unknown'
_J='accessible-for-notify'
_I='read-write'
_H='OctetString'
_G='h3cRrppRingID'
_F='h3cRrppDomainID'
_E='read-create'
_D='Integer32'
_C='A3COM-HUAWEI-RRPP-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
h3cRrpp=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,45))
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_H3cRrppScalarGroup_ObjectIdentity=ObjectIdentity
h3cRrppScalarGroup=_H3cRrppScalarGroup_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,45,1))
_H3cRrppEnableStatus_Type=EnabledStatus
_H3cRrppEnableStatus_Object=MibScalar
h3cRrppEnableStatus=_H3cRrppEnableStatus_Object((1,3,6,1,4,1,43,45,1,10,2,45,1,1),_H3cRrppEnableStatus_Type())
h3cRrppEnableStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cRrppEnableStatus.setStatus(_A)
class _H3cRrppPassword_Type(OctetString):defaultHexValue='303030464532303346443735';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_H3cRrppPassword_Type.__name__=_H
_H3cRrppPassword_Object=MibScalar
h3cRrppPassword=_H3cRrppPassword_Object((1,3,6,1,4,1,43,45,1,10,2,45,1,2),_H3cRrppPassword_Type())
h3cRrppPassword.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cRrppPassword.setStatus(_A)
class _H3cRrppPasswordType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('simple',1),('cipher',2)))
_H3cRrppPasswordType_Type.__name__=_D
_H3cRrppPasswordType_Object=MibScalar
h3cRrppPasswordType=_H3cRrppPasswordType_Object((1,3,6,1,4,1,43,45,1,10,2,45,1,3),_H3cRrppPasswordType_Type())
h3cRrppPasswordType.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cRrppPasswordType.setStatus(_A)
class _H3cRrppProtectVlanConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vlan',1),('instance',2)))
_H3cRrppProtectVlanConfigMode_Type.__name__=_D
_H3cRrppProtectVlanConfigMode_Object=MibScalar
h3cRrppProtectVlanConfigMode=_H3cRrppProtectVlanConfigMode_Object((1,3,6,1,4,1,43,45,1,10,2,45,1,4),_H3cRrppProtectVlanConfigMode_Type())
h3cRrppProtectVlanConfigMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRrppProtectVlanConfigMode.setStatus(_A)
_H3cRrppTable_ObjectIdentity=ObjectIdentity
h3cRrppTable=_H3cRrppTable_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,45,2))
_H3cRrppDomainTable_Object=MibTable
h3cRrppDomainTable=_H3cRrppDomainTable_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,1))
if mibBuilder.loadTexts:h3cRrppDomainTable.setStatus(_A)
_H3cRrppDomainEntry_Object=MibTableRow
h3cRrppDomainEntry=_H3cRrppDomainEntry_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,1,1))
h3cRrppDomainEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:h3cRrppDomainEntry.setStatus(_A)
class _H3cRrppDomainID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_H3cRrppDomainID_Type.__name__=_D
_H3cRrppDomainID_Object=MibTableColumn
h3cRrppDomainID=_H3cRrppDomainID_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,1,1,1),_H3cRrppDomainID_Type())
h3cRrppDomainID.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cRrppDomainID.setStatus(_A)
class _H3cRrppDomainControlVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094),ValueRangeConstraint(65535,65535))
_H3cRrppDomainControlVlanID_Type.__name__=_D
_H3cRrppDomainControlVlanID_Object=MibTableColumn
h3cRrppDomainControlVlanID=_H3cRrppDomainControlVlanID_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,1,1,2),_H3cRrppDomainControlVlanID_Type())
h3cRrppDomainControlVlanID.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRrppDomainControlVlanID.setStatus(_A)
class _H3cRrppDomainHelloTime_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_H3cRrppDomainHelloTime_Type.__name__=_D
_H3cRrppDomainHelloTime_Object=MibTableColumn
h3cRrppDomainHelloTime=_H3cRrppDomainHelloTime_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,1,1,3),_H3cRrppDomainHelloTime_Type())
h3cRrppDomainHelloTime.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRrppDomainHelloTime.setStatus(_A)
class _H3cRrppDomainFailTime_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,30))
_H3cRrppDomainFailTime_Type.__name__=_D
_H3cRrppDomainFailTime_Object=MibTableColumn
h3cRrppDomainFailTime=_H3cRrppDomainFailTime_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,1,1,4),_H3cRrppDomainFailTime_Type())
h3cRrppDomainFailTime.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRrppDomainFailTime.setStatus(_A)
_H3cRrppDomainRowStatus_Type=RowStatus
_H3cRrppDomainRowStatus_Object=MibTableColumn
h3cRrppDomainRowStatus=_H3cRrppDomainRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,1,1,5),_H3cRrppDomainRowStatus_Type())
h3cRrppDomainRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRrppDomainRowStatus.setStatus(_A)
class _H3cRrppDomainInstanceListLow_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_H3cRrppDomainInstanceListLow_Type.__name__=_H
_H3cRrppDomainInstanceListLow_Object=MibTableColumn
h3cRrppDomainInstanceListLow=_H3cRrppDomainInstanceListLow_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,1,1,6),_H3cRrppDomainInstanceListLow_Type())
h3cRrppDomainInstanceListLow.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRrppDomainInstanceListLow.setStatus(_A)
class _H3cRrppDomainInstanceListHigh_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_H3cRrppDomainInstanceListHigh_Type.__name__=_H
_H3cRrppDomainInstanceListHigh_Object=MibTableColumn
h3cRrppDomainInstanceListHigh=_H3cRrppDomainInstanceListHigh_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,1,1,7),_H3cRrppDomainInstanceListHigh_Type())
h3cRrppDomainInstanceListHigh.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRrppDomainInstanceListHigh.setStatus(_A)
class _H3cRrppDomainProtectVlanListLow_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_H3cRrppDomainProtectVlanListLow_Type.__name__=_H
_H3cRrppDomainProtectVlanListLow_Object=MibTableColumn
h3cRrppDomainProtectVlanListLow=_H3cRrppDomainProtectVlanListLow_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,1,1,8),_H3cRrppDomainProtectVlanListLow_Type())
h3cRrppDomainProtectVlanListLow.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRrppDomainProtectVlanListLow.setStatus(_A)
class _H3cRrppDomainProtectVlanListHigh_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_H3cRrppDomainProtectVlanListHigh_Type.__name__=_H
_H3cRrppDomainProtectVlanListHigh_Object=MibTableColumn
h3cRrppDomainProtectVlanListHigh=_H3cRrppDomainProtectVlanListHigh_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,1,1,9),_H3cRrppDomainProtectVlanListHigh_Type())
h3cRrppDomainProtectVlanListHigh.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRrppDomainProtectVlanListHigh.setStatus(_A)
_H3cRrppRingTable_Object=MibTable
h3cRrppRingTable=_H3cRrppRingTable_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,2))
if mibBuilder.loadTexts:h3cRrppRingTable.setStatus(_A)
_H3cRrppRingEntry_Object=MibTableRow
h3cRrppRingEntry=_H3cRrppRingEntry_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,2,1))
h3cRrppRingEntry.setIndexNames((0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:h3cRrppRingEntry.setStatus(_A)
class _H3cRrppRingID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_H3cRrppRingID_Type.__name__=_D
_H3cRrppRingID_Object=MibTableColumn
h3cRrppRingID=_H3cRrppRingID_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,2,1,1),_H3cRrppRingID_Type())
h3cRrppRingID.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cRrppRingID.setStatus(_A)
_H3cRrppRingEnableStatus_Type=EnabledStatus
_H3cRrppRingEnableStatus_Object=MibTableColumn
h3cRrppRingEnableStatus=_H3cRrppRingEnableStatus_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,2,1,2),_H3cRrppRingEnableStatus_Type())
h3cRrppRingEnableStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRrppRingEnableStatus.setStatus(_A)
class _H3cRrppRingActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_H3cRrppRingActive_Type.__name__=_D
_H3cRrppRingActive_Object=MibTableColumn
h3cRrppRingActive=_H3cRrppRingActive_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,2,1,3),_H3cRrppRingActive_Type())
h3cRrppRingActive.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRrppRingActive.setStatus(_A)
class _H3cRrppRingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('health',2),('fault',3)))
_H3cRrppRingState_Type.__name__=_D
_H3cRrppRingState_Object=MibTableColumn
h3cRrppRingState=_H3cRrppRingState_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,2,1,4),_H3cRrppRingState_Type())
h3cRrppRingState.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRrppRingState.setStatus(_A)
class _H3cRrppRingNodeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('master',1),('transit',2),('edge',3),('assistantEdge',4)))
_H3cRrppRingNodeMode_Type.__name__=_D
_H3cRrppRingNodeMode_Object=MibTableColumn
h3cRrppRingNodeMode=_H3cRrppRingNodeMode_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,2,1,5),_H3cRrppRingNodeMode_Type())
h3cRrppRingNodeMode.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRrppRingNodeMode.setStatus(_A)
_H3cRrppRingPrimaryPort_Type=Integer32
_H3cRrppRingPrimaryPort_Object=MibTableColumn
h3cRrppRingPrimaryPort=_H3cRrppRingPrimaryPort_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,2,1,6),_H3cRrppRingPrimaryPort_Type())
h3cRrppRingPrimaryPort.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRrppRingPrimaryPort.setStatus(_A)
_H3cRrppRingSecondaryPort_Type=Integer32
_H3cRrppRingSecondaryPort_Object=MibTableColumn
h3cRrppRingSecondaryPort=_H3cRrppRingSecondaryPort_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,2,1,7),_H3cRrppRingSecondaryPort_Type())
h3cRrppRingSecondaryPort.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRrppRingSecondaryPort.setStatus(_A)
class _H3cRrppRingLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('majorRing',1),('subRing',2)))
_H3cRrppRingLevel_Type.__name__=_D
_H3cRrppRingLevel_Object=MibTableColumn
h3cRrppRingLevel=_H3cRrppRingLevel_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,2,1,8),_H3cRrppRingLevel_Type())
h3cRrppRingLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRrppRingLevel.setStatus(_A)
_H3cRrppRingRowStatus_Type=RowStatus
_H3cRrppRingRowStatus_Object=MibTableColumn
h3cRrppRingRowStatus=_H3cRrppRingRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,2,1,9),_H3cRrppRingRowStatus_Type())
h3cRrppRingRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRrppRingRowStatus.setStatus(_A)
_H3cRrppPortTable_Object=MibTable
h3cRrppPortTable=_H3cRrppPortTable_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,3))
if mibBuilder.loadTexts:h3cRrppPortTable.setStatus(_A)
_H3cRrppPortEntry_Object=MibTableRow
h3cRrppPortEntry=_H3cRrppPortEntry_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,3,1))
h3cRrppPortEntry.setIndexNames((0,_C,_F),(0,_C,_G),(0,_C,_L))
if mibBuilder.loadTexts:h3cRrppPortEntry.setStatus(_A)
_H3cRrppPortID_Type=Integer32
_H3cRrppPortID_Object=MibTableColumn
h3cRrppPortID=_H3cRrppPortID_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,3,1,1),_H3cRrppPortID_Type())
h3cRrppPortID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:h3cRrppPortID.setStatus(_A)
class _H3cRrppPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('primary',1),('secondary',2),('common',3),('edge',4)))
_H3cRrppPortRole_Type.__name__=_D
_H3cRrppPortRole_Object=MibTableColumn
h3cRrppPortRole=_H3cRrppPortRole_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,3,1,2),_H3cRrppPortRole_Type())
h3cRrppPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRrppPortRole.setStatus(_A)
class _H3cRrppPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),('unblocked',2),('blocked',3),('down',4)))
_H3cRrppPortState_Type.__name__=_D
_H3cRrppPortState_Object=MibTableColumn
h3cRrppPortState=_H3cRrppPortState_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,3,1,3),_H3cRrppPortState_Type())
h3cRrppPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRrppPortState.setStatus(_A)
_H3cRrppPortRXError_Type=Counter32
_H3cRrppPortRXError_Object=MibTableColumn
h3cRrppPortRXError=_H3cRrppPortRXError_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,3,1,4),_H3cRrppPortRXError_Type())
h3cRrppPortRXError.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRrppPortRXError.setStatus(_A)
_H3cRrppPortRXHello_Type=Counter32
_H3cRrppPortRXHello_Object=MibTableColumn
h3cRrppPortRXHello=_H3cRrppPortRXHello_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,3,1,5),_H3cRrppPortRXHello_Type())
h3cRrppPortRXHello.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRrppPortRXHello.setStatus(_A)
_H3cRrppPortRXLinkUp_Type=Counter32
_H3cRrppPortRXLinkUp_Object=MibTableColumn
h3cRrppPortRXLinkUp=_H3cRrppPortRXLinkUp_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,3,1,6),_H3cRrppPortRXLinkUp_Type())
h3cRrppPortRXLinkUp.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRrppPortRXLinkUp.setStatus(_A)
_H3cRrppPortRXLinkDown_Type=Counter32
_H3cRrppPortRXLinkDown_Object=MibTableColumn
h3cRrppPortRXLinkDown=_H3cRrppPortRXLinkDown_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,3,1,7),_H3cRrppPortRXLinkDown_Type())
h3cRrppPortRXLinkDown.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRrppPortRXLinkDown.setStatus(_A)
_H3cRrppPortRXCommonFlush_Type=Counter32
_H3cRrppPortRXCommonFlush_Object=MibTableColumn
h3cRrppPortRXCommonFlush=_H3cRrppPortRXCommonFlush_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,3,1,8),_H3cRrppPortRXCommonFlush_Type())
h3cRrppPortRXCommonFlush.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRrppPortRXCommonFlush.setStatus(_A)
_H3cRrppPortRXCompleteFlush_Type=Counter32
_H3cRrppPortRXCompleteFlush_Object=MibTableColumn
h3cRrppPortRXCompleteFlush=_H3cRrppPortRXCompleteFlush_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,3,1,9),_H3cRrppPortRXCompleteFlush_Type())
h3cRrppPortRXCompleteFlush.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRrppPortRXCompleteFlush.setStatus(_A)
_H3cRrppPortTXHello_Type=Counter32
_H3cRrppPortTXHello_Object=MibTableColumn
h3cRrppPortTXHello=_H3cRrppPortTXHello_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,3,1,10),_H3cRrppPortTXHello_Type())
h3cRrppPortTXHello.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRrppPortTXHello.setStatus(_A)
_H3cRrppPortTXLinkUp_Type=Counter32
_H3cRrppPortTXLinkUp_Object=MibTableColumn
h3cRrppPortTXLinkUp=_H3cRrppPortTXLinkUp_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,3,1,11),_H3cRrppPortTXLinkUp_Type())
h3cRrppPortTXLinkUp.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRrppPortTXLinkUp.setStatus(_A)
_H3cRrppPortTXLinkDown_Type=Counter32
_H3cRrppPortTXLinkDown_Object=MibTableColumn
h3cRrppPortTXLinkDown=_H3cRrppPortTXLinkDown_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,3,1,12),_H3cRrppPortTXLinkDown_Type())
h3cRrppPortTXLinkDown.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRrppPortTXLinkDown.setStatus(_A)
_H3cRrppPortTXCommonFlush_Type=Counter32
_H3cRrppPortTXCommonFlush_Object=MibTableColumn
h3cRrppPortTXCommonFlush=_H3cRrppPortTXCommonFlush_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,3,1,13),_H3cRrppPortTXCommonFlush_Type())
h3cRrppPortTXCommonFlush.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRrppPortTXCommonFlush.setStatus(_A)
_H3cRrppPortTXCompleteFlush_Type=Counter32
_H3cRrppPortTXCompleteFlush_Object=MibTableColumn
h3cRrppPortTXCompleteFlush=_H3cRrppPortTXCompleteFlush_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,3,1,14),_H3cRrppPortTXCompleteFlush_Type())
h3cRrppPortTXCompleteFlush.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRrppPortTXCompleteFlush.setStatus(_A)
_H3cRrppPortRXEdgeHello_Type=Counter32
_H3cRrppPortRXEdgeHello_Object=MibTableColumn
h3cRrppPortRXEdgeHello=_H3cRrppPortRXEdgeHello_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,3,1,15),_H3cRrppPortRXEdgeHello_Type())
h3cRrppPortRXEdgeHello.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRrppPortRXEdgeHello.setStatus(_A)
_H3cRrppPortRXMajorFault_Type=Counter32
_H3cRrppPortRXMajorFault_Object=MibTableColumn
h3cRrppPortRXMajorFault=_H3cRrppPortRXMajorFault_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,3,1,16),_H3cRrppPortRXMajorFault_Type())
h3cRrppPortRXMajorFault.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRrppPortRXMajorFault.setStatus(_A)
_H3cRrppPortTXEdgeHello_Type=Counter32
_H3cRrppPortTXEdgeHello_Object=MibTableColumn
h3cRrppPortTXEdgeHello=_H3cRrppPortTXEdgeHello_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,3,1,17),_H3cRrppPortTXEdgeHello_Type())
h3cRrppPortTXEdgeHello.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRrppPortTXEdgeHello.setStatus(_A)
_H3cRrppPortTXMajorFault_Type=Counter32
_H3cRrppPortTXMajorFault_Object=MibTableColumn
h3cRrppPortTXMajorFault=_H3cRrppPortTXMajorFault_Object((1,3,6,1,4,1,43,45,1,10,2,45,2,3,1,18),_H3cRrppPortTXMajorFault_Type())
h3cRrppPortTXMajorFault.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRrppPortTXMajorFault.setStatus(_A)
_H3cRrppNotifications_ObjectIdentity=ObjectIdentity
h3cRrppNotifications=_H3cRrppNotifications_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,45,3))
h3cRrppRingRecover=NotificationType((1,3,6,1,4,1,43,45,1,10,2,45,3,1))
h3cRrppRingRecover.setObjects(*((_C,_F),(_C,_G)))
if mibBuilder.loadTexts:h3cRrppRingRecover.setStatus(_A)
h3cRrppRingFail=NotificationType((1,3,6,1,4,1,43,45,1,10,2,45,3,2))
h3cRrppRingFail.setObjects(*((_C,_F),(_C,_G)))
if mibBuilder.loadTexts:h3cRrppRingFail.setStatus(_A)
h3cRrppMultiMaster=NotificationType((1,3,6,1,4,1,43,45,1,10,2,45,3,3))
h3cRrppMultiMaster.setObjects(*((_C,_F),(_C,_G)))
if mibBuilder.loadTexts:h3cRrppMultiMaster.setStatus(_A)
h3cRrppMajorFault=NotificationType((1,3,6,1,4,1,43,45,1,10,2,45,3,4))
h3cRrppMajorFault.setObjects(*((_C,_F),(_C,_G)))
if mibBuilder.loadTexts:h3cRrppMajorFault.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'EnabledStatus':EnabledStatus,'h3cRrpp':h3cRrpp,'h3cRrppScalarGroup':h3cRrppScalarGroup,'h3cRrppEnableStatus':h3cRrppEnableStatus,'h3cRrppPassword':h3cRrppPassword,'h3cRrppPasswordType':h3cRrppPasswordType,'h3cRrppProtectVlanConfigMode':h3cRrppProtectVlanConfigMode,'h3cRrppTable':h3cRrppTable,'h3cRrppDomainTable':h3cRrppDomainTable,'h3cRrppDomainEntry':h3cRrppDomainEntry,_F:h3cRrppDomainID,'h3cRrppDomainControlVlanID':h3cRrppDomainControlVlanID,'h3cRrppDomainHelloTime':h3cRrppDomainHelloTime,'h3cRrppDomainFailTime':h3cRrppDomainFailTime,'h3cRrppDomainRowStatus':h3cRrppDomainRowStatus,'h3cRrppDomainInstanceListLow':h3cRrppDomainInstanceListLow,'h3cRrppDomainInstanceListHigh':h3cRrppDomainInstanceListHigh,'h3cRrppDomainProtectVlanListLow':h3cRrppDomainProtectVlanListLow,'h3cRrppDomainProtectVlanListHigh':h3cRrppDomainProtectVlanListHigh,'h3cRrppRingTable':h3cRrppRingTable,'h3cRrppRingEntry':h3cRrppRingEntry,_G:h3cRrppRingID,'h3cRrppRingEnableStatus':h3cRrppRingEnableStatus,'h3cRrppRingActive':h3cRrppRingActive,'h3cRrppRingState':h3cRrppRingState,'h3cRrppRingNodeMode':h3cRrppRingNodeMode,'h3cRrppRingPrimaryPort':h3cRrppRingPrimaryPort,'h3cRrppRingSecondaryPort':h3cRrppRingSecondaryPort,'h3cRrppRingLevel':h3cRrppRingLevel,'h3cRrppRingRowStatus':h3cRrppRingRowStatus,'h3cRrppPortTable':h3cRrppPortTable,'h3cRrppPortEntry':h3cRrppPortEntry,_L:h3cRrppPortID,'h3cRrppPortRole':h3cRrppPortRole,'h3cRrppPortState':h3cRrppPortState,'h3cRrppPortRXError':h3cRrppPortRXError,'h3cRrppPortRXHello':h3cRrppPortRXHello,'h3cRrppPortRXLinkUp':h3cRrppPortRXLinkUp,'h3cRrppPortRXLinkDown':h3cRrppPortRXLinkDown,'h3cRrppPortRXCommonFlush':h3cRrppPortRXCommonFlush,'h3cRrppPortRXCompleteFlush':h3cRrppPortRXCompleteFlush,'h3cRrppPortTXHello':h3cRrppPortTXHello,'h3cRrppPortTXLinkUp':h3cRrppPortTXLinkUp,'h3cRrppPortTXLinkDown':h3cRrppPortTXLinkDown,'h3cRrppPortTXCommonFlush':h3cRrppPortTXCommonFlush,'h3cRrppPortTXCompleteFlush':h3cRrppPortTXCompleteFlush,'h3cRrppPortRXEdgeHello':h3cRrppPortRXEdgeHello,'h3cRrppPortRXMajorFault':h3cRrppPortRXMajorFault,'h3cRrppPortTXEdgeHello':h3cRrppPortTXEdgeHello,'h3cRrppPortTXMajorFault':h3cRrppPortTXMajorFault,'h3cRrppNotifications':h3cRrppNotifications,'h3cRrppRingRecover':h3cRrppRingRecover,'h3cRrppRingFail':h3cRrppRingFail,'h3cRrppMultiMaster':h3cRrppMultiMaster,'h3cRrppMajorFault':h3cRrppMajorFault})