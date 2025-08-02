_L='hpnicfRrppPortID'
_K='unknown'
_J='accessible-for-notify'
_I='read-write'
_H='OctetString'
_G='hpnicfRrppRingID'
_F='hpnicfRrppDomainID'
_E='read-create'
_D='Integer32'
_C='HPN-ICF-RRPP-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpnicfRrpp=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,45))
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_HpnicfRrppScalarGroup_ObjectIdentity=ObjectIdentity
hpnicfRrppScalarGroup=_HpnicfRrppScalarGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,45,1))
_HpnicfRrppEnableStatus_Type=EnabledStatus
_HpnicfRrppEnableStatus_Object=MibScalar
hpnicfRrppEnableStatus=_HpnicfRrppEnableStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,1,1),_HpnicfRrppEnableStatus_Type())
hpnicfRrppEnableStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfRrppEnableStatus.setStatus(_A)
class _HpnicfRrppPassword_Type(OctetString):defaultHexValue='303030464532303346443735';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_HpnicfRrppPassword_Type.__name__=_H
_HpnicfRrppPassword_Object=MibScalar
hpnicfRrppPassword=_HpnicfRrppPassword_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,1,2),_HpnicfRrppPassword_Type())
hpnicfRrppPassword.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfRrppPassword.setStatus(_A)
class _HpnicfRrppPasswordType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('simple',1),('cipher',2)))
_HpnicfRrppPasswordType_Type.__name__=_D
_HpnicfRrppPasswordType_Object=MibScalar
hpnicfRrppPasswordType=_HpnicfRrppPasswordType_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,1,3),_HpnicfRrppPasswordType_Type())
hpnicfRrppPasswordType.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfRrppPasswordType.setStatus(_A)
class _HpnicfRrppProtectVlanConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vlan',1),('instance',2)))
_HpnicfRrppProtectVlanConfigMode_Type.__name__=_D
_HpnicfRrppProtectVlanConfigMode_Object=MibScalar
hpnicfRrppProtectVlanConfigMode=_HpnicfRrppProtectVlanConfigMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,1,4),_HpnicfRrppProtectVlanConfigMode_Type())
hpnicfRrppProtectVlanConfigMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRrppProtectVlanConfigMode.setStatus(_A)
_HpnicfRrppTable_ObjectIdentity=ObjectIdentity
hpnicfRrppTable=_HpnicfRrppTable_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,45,2))
_HpnicfRrppDomainTable_Object=MibTable
hpnicfRrppDomainTable=_HpnicfRrppDomainTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,1))
if mibBuilder.loadTexts:hpnicfRrppDomainTable.setStatus(_A)
_HpnicfRrppDomainEntry_Object=MibTableRow
hpnicfRrppDomainEntry=_HpnicfRrppDomainEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,1,1))
hpnicfRrppDomainEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:hpnicfRrppDomainEntry.setStatus(_A)
class _HpnicfRrppDomainID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HpnicfRrppDomainID_Type.__name__=_D
_HpnicfRrppDomainID_Object=MibTableColumn
hpnicfRrppDomainID=_HpnicfRrppDomainID_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,1,1,1),_HpnicfRrppDomainID_Type())
hpnicfRrppDomainID.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfRrppDomainID.setStatus(_A)
class _HpnicfRrppDomainControlVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094),ValueRangeConstraint(65535,65535))
_HpnicfRrppDomainControlVlanID_Type.__name__=_D
_HpnicfRrppDomainControlVlanID_Object=MibTableColumn
hpnicfRrppDomainControlVlanID=_HpnicfRrppDomainControlVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,1,1,2),_HpnicfRrppDomainControlVlanID_Type())
hpnicfRrppDomainControlVlanID.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRrppDomainControlVlanID.setStatus(_A)
class _HpnicfRrppDomainHelloTime_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_HpnicfRrppDomainHelloTime_Type.__name__=_D
_HpnicfRrppDomainHelloTime_Object=MibTableColumn
hpnicfRrppDomainHelloTime=_HpnicfRrppDomainHelloTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,1,1,3),_HpnicfRrppDomainHelloTime_Type())
hpnicfRrppDomainHelloTime.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRrppDomainHelloTime.setStatus(_A)
class _HpnicfRrppDomainFailTime_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,30))
_HpnicfRrppDomainFailTime_Type.__name__=_D
_HpnicfRrppDomainFailTime_Object=MibTableColumn
hpnicfRrppDomainFailTime=_HpnicfRrppDomainFailTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,1,1,4),_HpnicfRrppDomainFailTime_Type())
hpnicfRrppDomainFailTime.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRrppDomainFailTime.setStatus(_A)
_HpnicfRrppDomainRowStatus_Type=RowStatus
_HpnicfRrppDomainRowStatus_Object=MibTableColumn
hpnicfRrppDomainRowStatus=_HpnicfRrppDomainRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,1,1,5),_HpnicfRrppDomainRowStatus_Type())
hpnicfRrppDomainRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRrppDomainRowStatus.setStatus(_A)
class _HpnicfRrppDomainInstanceListLow_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_HpnicfRrppDomainInstanceListLow_Type.__name__=_H
_HpnicfRrppDomainInstanceListLow_Object=MibTableColumn
hpnicfRrppDomainInstanceListLow=_HpnicfRrppDomainInstanceListLow_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,1,1,6),_HpnicfRrppDomainInstanceListLow_Type())
hpnicfRrppDomainInstanceListLow.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRrppDomainInstanceListLow.setStatus(_A)
class _HpnicfRrppDomainInstanceListHigh_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_HpnicfRrppDomainInstanceListHigh_Type.__name__=_H
_HpnicfRrppDomainInstanceListHigh_Object=MibTableColumn
hpnicfRrppDomainInstanceListHigh=_HpnicfRrppDomainInstanceListHigh_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,1,1,7),_HpnicfRrppDomainInstanceListHigh_Type())
hpnicfRrppDomainInstanceListHigh.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRrppDomainInstanceListHigh.setStatus(_A)
class _HpnicfRrppDomainProtectVlanListLow_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_HpnicfRrppDomainProtectVlanListLow_Type.__name__=_H
_HpnicfRrppDomainProtectVlanListLow_Object=MibTableColumn
hpnicfRrppDomainProtectVlanListLow=_HpnicfRrppDomainProtectVlanListLow_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,1,1,8),_HpnicfRrppDomainProtectVlanListLow_Type())
hpnicfRrppDomainProtectVlanListLow.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRrppDomainProtectVlanListLow.setStatus(_A)
class _HpnicfRrppDomainProtectVlanListHigh_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_HpnicfRrppDomainProtectVlanListHigh_Type.__name__=_H
_HpnicfRrppDomainProtectVlanListHigh_Object=MibTableColumn
hpnicfRrppDomainProtectVlanListHigh=_HpnicfRrppDomainProtectVlanListHigh_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,1,1,9),_HpnicfRrppDomainProtectVlanListHigh_Type())
hpnicfRrppDomainProtectVlanListHigh.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRrppDomainProtectVlanListHigh.setStatus(_A)
_HpnicfRrppRingTable_Object=MibTable
hpnicfRrppRingTable=_HpnicfRrppRingTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,2))
if mibBuilder.loadTexts:hpnicfRrppRingTable.setStatus(_A)
_HpnicfRrppRingEntry_Object=MibTableRow
hpnicfRrppRingEntry=_HpnicfRrppRingEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,2,1))
hpnicfRrppRingEntry.setIndexNames((0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:hpnicfRrppRingEntry.setStatus(_A)
class _HpnicfRrppRingID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_HpnicfRrppRingID_Type.__name__=_D
_HpnicfRrppRingID_Object=MibTableColumn
hpnicfRrppRingID=_HpnicfRrppRingID_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,2,1,1),_HpnicfRrppRingID_Type())
hpnicfRrppRingID.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfRrppRingID.setStatus(_A)
_HpnicfRrppRingEnableStatus_Type=EnabledStatus
_HpnicfRrppRingEnableStatus_Object=MibTableColumn
hpnicfRrppRingEnableStatus=_HpnicfRrppRingEnableStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,2,1,2),_HpnicfRrppRingEnableStatus_Type())
hpnicfRrppRingEnableStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRrppRingEnableStatus.setStatus(_A)
class _HpnicfRrppRingActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_HpnicfRrppRingActive_Type.__name__=_D
_HpnicfRrppRingActive_Object=MibTableColumn
hpnicfRrppRingActive=_HpnicfRrppRingActive_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,2,1,3),_HpnicfRrppRingActive_Type())
hpnicfRrppRingActive.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRrppRingActive.setStatus(_A)
class _HpnicfRrppRingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('health',2),('fault',3)))
_HpnicfRrppRingState_Type.__name__=_D
_HpnicfRrppRingState_Object=MibTableColumn
hpnicfRrppRingState=_HpnicfRrppRingState_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,2,1,4),_HpnicfRrppRingState_Type())
hpnicfRrppRingState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRrppRingState.setStatus(_A)
class _HpnicfRrppRingNodeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('master',1),('transit',2),('edge',3),('assistantEdge',4)))
_HpnicfRrppRingNodeMode_Type.__name__=_D
_HpnicfRrppRingNodeMode_Object=MibTableColumn
hpnicfRrppRingNodeMode=_HpnicfRrppRingNodeMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,2,1,5),_HpnicfRrppRingNodeMode_Type())
hpnicfRrppRingNodeMode.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRrppRingNodeMode.setStatus(_A)
_HpnicfRrppRingPrimaryPort_Type=Integer32
_HpnicfRrppRingPrimaryPort_Object=MibTableColumn
hpnicfRrppRingPrimaryPort=_HpnicfRrppRingPrimaryPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,2,1,6),_HpnicfRrppRingPrimaryPort_Type())
hpnicfRrppRingPrimaryPort.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRrppRingPrimaryPort.setStatus(_A)
_HpnicfRrppRingSecondaryPort_Type=Integer32
_HpnicfRrppRingSecondaryPort_Object=MibTableColumn
hpnicfRrppRingSecondaryPort=_HpnicfRrppRingSecondaryPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,2,1,7),_HpnicfRrppRingSecondaryPort_Type())
hpnicfRrppRingSecondaryPort.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRrppRingSecondaryPort.setStatus(_A)
class _HpnicfRrppRingLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('majorRing',1),('subRing',2)))
_HpnicfRrppRingLevel_Type.__name__=_D
_HpnicfRrppRingLevel_Object=MibTableColumn
hpnicfRrppRingLevel=_HpnicfRrppRingLevel_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,2,1,8),_HpnicfRrppRingLevel_Type())
hpnicfRrppRingLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRrppRingLevel.setStatus(_A)
_HpnicfRrppRingRowStatus_Type=RowStatus
_HpnicfRrppRingRowStatus_Object=MibTableColumn
hpnicfRrppRingRowStatus=_HpnicfRrppRingRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,2,1,9),_HpnicfRrppRingRowStatus_Type())
hpnicfRrppRingRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRrppRingRowStatus.setStatus(_A)
_HpnicfRrppPortTable_Object=MibTable
hpnicfRrppPortTable=_HpnicfRrppPortTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,3))
if mibBuilder.loadTexts:hpnicfRrppPortTable.setStatus(_A)
_HpnicfRrppPortEntry_Object=MibTableRow
hpnicfRrppPortEntry=_HpnicfRrppPortEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,3,1))
hpnicfRrppPortEntry.setIndexNames((0,_C,_F),(0,_C,_G),(0,_C,_L))
if mibBuilder.loadTexts:hpnicfRrppPortEntry.setStatus(_A)
_HpnicfRrppPortID_Type=Integer32
_HpnicfRrppPortID_Object=MibTableColumn
hpnicfRrppPortID=_HpnicfRrppPortID_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,3,1,1),_HpnicfRrppPortID_Type())
hpnicfRrppPortID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpnicfRrppPortID.setStatus(_A)
class _HpnicfRrppPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('primary',1),('secondary',2),('common',3),('edge',4)))
_HpnicfRrppPortRole_Type.__name__=_D
_HpnicfRrppPortRole_Object=MibTableColumn
hpnicfRrppPortRole=_HpnicfRrppPortRole_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,3,1,2),_HpnicfRrppPortRole_Type())
hpnicfRrppPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRrppPortRole.setStatus(_A)
class _HpnicfRrppPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),('unblocked',2),('blocked',3),('down',4)))
_HpnicfRrppPortState_Type.__name__=_D
_HpnicfRrppPortState_Object=MibTableColumn
hpnicfRrppPortState=_HpnicfRrppPortState_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,3,1,3),_HpnicfRrppPortState_Type())
hpnicfRrppPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRrppPortState.setStatus(_A)
_HpnicfRrppPortRXError_Type=Counter32
_HpnicfRrppPortRXError_Object=MibTableColumn
hpnicfRrppPortRXError=_HpnicfRrppPortRXError_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,3,1,4),_HpnicfRrppPortRXError_Type())
hpnicfRrppPortRXError.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRrppPortRXError.setStatus(_A)
_HpnicfRrppPortRXHello_Type=Counter32
_HpnicfRrppPortRXHello_Object=MibTableColumn
hpnicfRrppPortRXHello=_HpnicfRrppPortRXHello_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,3,1,5),_HpnicfRrppPortRXHello_Type())
hpnicfRrppPortRXHello.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRrppPortRXHello.setStatus(_A)
_HpnicfRrppPortRXLinkUp_Type=Counter32
_HpnicfRrppPortRXLinkUp_Object=MibTableColumn
hpnicfRrppPortRXLinkUp=_HpnicfRrppPortRXLinkUp_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,3,1,6),_HpnicfRrppPortRXLinkUp_Type())
hpnicfRrppPortRXLinkUp.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRrppPortRXLinkUp.setStatus(_A)
_HpnicfRrppPortRXLinkDown_Type=Counter32
_HpnicfRrppPortRXLinkDown_Object=MibTableColumn
hpnicfRrppPortRXLinkDown=_HpnicfRrppPortRXLinkDown_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,3,1,7),_HpnicfRrppPortRXLinkDown_Type())
hpnicfRrppPortRXLinkDown.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRrppPortRXLinkDown.setStatus(_A)
_HpnicfRrppPortRXCommonFlush_Type=Counter32
_HpnicfRrppPortRXCommonFlush_Object=MibTableColumn
hpnicfRrppPortRXCommonFlush=_HpnicfRrppPortRXCommonFlush_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,3,1,8),_HpnicfRrppPortRXCommonFlush_Type())
hpnicfRrppPortRXCommonFlush.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRrppPortRXCommonFlush.setStatus(_A)
_HpnicfRrppPortRXCompleteFlush_Type=Counter32
_HpnicfRrppPortRXCompleteFlush_Object=MibTableColumn
hpnicfRrppPortRXCompleteFlush=_HpnicfRrppPortRXCompleteFlush_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,3,1,9),_HpnicfRrppPortRXCompleteFlush_Type())
hpnicfRrppPortRXCompleteFlush.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRrppPortRXCompleteFlush.setStatus(_A)
_HpnicfRrppPortTXHello_Type=Counter32
_HpnicfRrppPortTXHello_Object=MibTableColumn
hpnicfRrppPortTXHello=_HpnicfRrppPortTXHello_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,3,1,10),_HpnicfRrppPortTXHello_Type())
hpnicfRrppPortTXHello.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRrppPortTXHello.setStatus(_A)
_HpnicfRrppPortTXLinkUp_Type=Counter32
_HpnicfRrppPortTXLinkUp_Object=MibTableColumn
hpnicfRrppPortTXLinkUp=_HpnicfRrppPortTXLinkUp_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,3,1,11),_HpnicfRrppPortTXLinkUp_Type())
hpnicfRrppPortTXLinkUp.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRrppPortTXLinkUp.setStatus(_A)
_HpnicfRrppPortTXLinkDown_Type=Counter32
_HpnicfRrppPortTXLinkDown_Object=MibTableColumn
hpnicfRrppPortTXLinkDown=_HpnicfRrppPortTXLinkDown_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,3,1,12),_HpnicfRrppPortTXLinkDown_Type())
hpnicfRrppPortTXLinkDown.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRrppPortTXLinkDown.setStatus(_A)
_HpnicfRrppPortTXCommonFlush_Type=Counter32
_HpnicfRrppPortTXCommonFlush_Object=MibTableColumn
hpnicfRrppPortTXCommonFlush=_HpnicfRrppPortTXCommonFlush_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,3,1,13),_HpnicfRrppPortTXCommonFlush_Type())
hpnicfRrppPortTXCommonFlush.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRrppPortTXCommonFlush.setStatus(_A)
_HpnicfRrppPortTXCompleteFlush_Type=Counter32
_HpnicfRrppPortTXCompleteFlush_Object=MibTableColumn
hpnicfRrppPortTXCompleteFlush=_HpnicfRrppPortTXCompleteFlush_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,3,1,14),_HpnicfRrppPortTXCompleteFlush_Type())
hpnicfRrppPortTXCompleteFlush.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRrppPortTXCompleteFlush.setStatus(_A)
_HpnicfRrppPortRXEdgeHello_Type=Counter32
_HpnicfRrppPortRXEdgeHello_Object=MibTableColumn
hpnicfRrppPortRXEdgeHello=_HpnicfRrppPortRXEdgeHello_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,3,1,15),_HpnicfRrppPortRXEdgeHello_Type())
hpnicfRrppPortRXEdgeHello.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRrppPortRXEdgeHello.setStatus(_A)
_HpnicfRrppPortRXMajorFault_Type=Counter32
_HpnicfRrppPortRXMajorFault_Object=MibTableColumn
hpnicfRrppPortRXMajorFault=_HpnicfRrppPortRXMajorFault_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,3,1,16),_HpnicfRrppPortRXMajorFault_Type())
hpnicfRrppPortRXMajorFault.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRrppPortRXMajorFault.setStatus(_A)
_HpnicfRrppPortTXEdgeHello_Type=Counter32
_HpnicfRrppPortTXEdgeHello_Object=MibTableColumn
hpnicfRrppPortTXEdgeHello=_HpnicfRrppPortTXEdgeHello_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,3,1,17),_HpnicfRrppPortTXEdgeHello_Type())
hpnicfRrppPortTXEdgeHello.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRrppPortTXEdgeHello.setStatus(_A)
_HpnicfRrppPortTXMajorFault_Type=Counter32
_HpnicfRrppPortTXMajorFault_Object=MibTableColumn
hpnicfRrppPortTXMajorFault=_HpnicfRrppPortTXMajorFault_Object((1,3,6,1,4,1,11,2,14,11,15,2,45,2,3,1,18),_HpnicfRrppPortTXMajorFault_Type())
hpnicfRrppPortTXMajorFault.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRrppPortTXMajorFault.setStatus(_A)
_HpnicfRrppNotifications_ObjectIdentity=ObjectIdentity
hpnicfRrppNotifications=_HpnicfRrppNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,45,3))
hpnicfRrppRingRecover=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,45,3,1))
hpnicfRrppRingRecover.setObjects(*((_C,_F),(_C,_G)))
if mibBuilder.loadTexts:hpnicfRrppRingRecover.setStatus(_A)
hpnicfRrppRingFail=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,45,3,2))
hpnicfRrppRingFail.setObjects(*((_C,_F),(_C,_G)))
if mibBuilder.loadTexts:hpnicfRrppRingFail.setStatus(_A)
hpnicfRrppMultiMaster=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,45,3,3))
hpnicfRrppMultiMaster.setObjects(*((_C,_F),(_C,_G)))
if mibBuilder.loadTexts:hpnicfRrppMultiMaster.setStatus(_A)
hpnicfRrppMajorFault=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,45,3,4))
hpnicfRrppMajorFault.setObjects(*((_C,_F),(_C,_G)))
if mibBuilder.loadTexts:hpnicfRrppMajorFault.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'EnabledStatus':EnabledStatus,'hpnicfRrpp':hpnicfRrpp,'hpnicfRrppScalarGroup':hpnicfRrppScalarGroup,'hpnicfRrppEnableStatus':hpnicfRrppEnableStatus,'hpnicfRrppPassword':hpnicfRrppPassword,'hpnicfRrppPasswordType':hpnicfRrppPasswordType,'hpnicfRrppProtectVlanConfigMode':hpnicfRrppProtectVlanConfigMode,'hpnicfRrppTable':hpnicfRrppTable,'hpnicfRrppDomainTable':hpnicfRrppDomainTable,'hpnicfRrppDomainEntry':hpnicfRrppDomainEntry,_F:hpnicfRrppDomainID,'hpnicfRrppDomainControlVlanID':hpnicfRrppDomainControlVlanID,'hpnicfRrppDomainHelloTime':hpnicfRrppDomainHelloTime,'hpnicfRrppDomainFailTime':hpnicfRrppDomainFailTime,'hpnicfRrppDomainRowStatus':hpnicfRrppDomainRowStatus,'hpnicfRrppDomainInstanceListLow':hpnicfRrppDomainInstanceListLow,'hpnicfRrppDomainInstanceListHigh':hpnicfRrppDomainInstanceListHigh,'hpnicfRrppDomainProtectVlanListLow':hpnicfRrppDomainProtectVlanListLow,'hpnicfRrppDomainProtectVlanListHigh':hpnicfRrppDomainProtectVlanListHigh,'hpnicfRrppRingTable':hpnicfRrppRingTable,'hpnicfRrppRingEntry':hpnicfRrppRingEntry,_G:hpnicfRrppRingID,'hpnicfRrppRingEnableStatus':hpnicfRrppRingEnableStatus,'hpnicfRrppRingActive':hpnicfRrppRingActive,'hpnicfRrppRingState':hpnicfRrppRingState,'hpnicfRrppRingNodeMode':hpnicfRrppRingNodeMode,'hpnicfRrppRingPrimaryPort':hpnicfRrppRingPrimaryPort,'hpnicfRrppRingSecondaryPort':hpnicfRrppRingSecondaryPort,'hpnicfRrppRingLevel':hpnicfRrppRingLevel,'hpnicfRrppRingRowStatus':hpnicfRrppRingRowStatus,'hpnicfRrppPortTable':hpnicfRrppPortTable,'hpnicfRrppPortEntry':hpnicfRrppPortEntry,_L:hpnicfRrppPortID,'hpnicfRrppPortRole':hpnicfRrppPortRole,'hpnicfRrppPortState':hpnicfRrppPortState,'hpnicfRrppPortRXError':hpnicfRrppPortRXError,'hpnicfRrppPortRXHello':hpnicfRrppPortRXHello,'hpnicfRrppPortRXLinkUp':hpnicfRrppPortRXLinkUp,'hpnicfRrppPortRXLinkDown':hpnicfRrppPortRXLinkDown,'hpnicfRrppPortRXCommonFlush':hpnicfRrppPortRXCommonFlush,'hpnicfRrppPortRXCompleteFlush':hpnicfRrppPortRXCompleteFlush,'hpnicfRrppPortTXHello':hpnicfRrppPortTXHello,'hpnicfRrppPortTXLinkUp':hpnicfRrppPortTXLinkUp,'hpnicfRrppPortTXLinkDown':hpnicfRrppPortTXLinkDown,'hpnicfRrppPortTXCommonFlush':hpnicfRrppPortTXCommonFlush,'hpnicfRrppPortTXCompleteFlush':hpnicfRrppPortTXCompleteFlush,'hpnicfRrppPortRXEdgeHello':hpnicfRrppPortRXEdgeHello,'hpnicfRrppPortRXMajorFault':hpnicfRrppPortRXMajorFault,'hpnicfRrppPortTXEdgeHello':hpnicfRrppPortTXEdgeHello,'hpnicfRrppPortTXMajorFault':hpnicfRrppPortTXMajorFault,'hpnicfRrppNotifications':hpnicfRrppNotifications,'hpnicfRrppRingRecover':hpnicfRrppRingRecover,'hpnicfRrppRingFail':hpnicfRrppRingFail,'hpnicfRrppMultiMaster':hpnicfRrppMultiMaster,'hpnicfRrppMajorFault':hpnicfRrppMajorFault})