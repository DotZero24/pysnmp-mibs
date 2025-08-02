_A2='aipLLDPConfigManAddrEntryGroup'
_A1='aipLLDPConfGroup'
_A0='aipNotificationGroup'
_z='aipAMAPConfGroup'
_y='aipGMAPConfGroup'
_x='aipGMAPConflictTrap'
_w='aipAMAPStatusTrap'
_v='aipLLDPConfigManAddrTlvTxEnable'
_u='aipLLDPDestMac'
_t='aipAMAPRemPort'
_s='aipAMAPRemSlot'
_r='aipAMAPLocalPort'
_q='aipAMAPLocalSlot'
_p='aipAMAPLocalIfindex'
_o='aipAMAPVoiceVlan'
_n='aipAMAPRemHostname'
_m='aipAMAPRemVlan'
_l='aipAMAPportstatus'
_k='aipAMAPcommontime'
_j='aipAMAPdisctime'
_i='aipAMAPstate'
_h='aipGMAPTimeout'
_g='aipGMAPFlags'
_f='aipGMAPSrcSwitch'
_e='aipGMAPVlan'
_d='aipGMAPholdtime'
_c='aipGMAPupdatetime'
_b='aipGMAPgaptime'
_a='aipGMAPstate'
_Z='aipLLDPConfigManAddrPortNum'
_Y='ipPhone'
_X='inactive'
_W='active'
_V='TruthValue'
_U='OctetString'
_T='aipAMAPLastTrapPort'
_S='aipAMAPLastTrapReason'
_R='aipGMAPLastTrapVlan'
_Q='aipGMAPLastTrapProtocol'
_P='aipGMAPLastTrapMac'
_O='aipGMAPLastTrapPort'
_N='aipGMAPLastTrapReason'
_M='aipAMAPIpAddr'
_L='aipAMAPHostMac'
_K='aipAMAPRemConnectionIndex'
_J='aipAMAPRemMac'
_I='aipAMAPLocalConnectionIndex'
_H='aipGMAPProtocol'
_G='aipGMAPMacAddr'
_F='DisplayString'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='current'
_A='ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_U,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aipAMAPTraps,aipGMAPTraps,softentIND1Aip=mibBuilder.importSymbols('ALCATEL-IND1-BASE','aipAMAPTraps','aipGMAPTraps','softentIND1Aip')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','TextualConvention',_V)
alcatelIND1InterswitchProtocolMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,9,1))
if mibBuilder.loadTexts:alcatelIND1InterswitchProtocolMIB.setRevisions(('2011-05-06 00:00','2009-02-21 00:00','2007-04-03 00:00'))
_AlcatelIND1InterswitchProtocolMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1InterswitchProtocolMIBObjects=_AlcatelIND1InterswitchProtocolMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,9,1,1))
_AipGMAPconfig_ObjectIdentity=ObjectIdentity
aipGMAPconfig=_AipGMAPconfig_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,1))
class _AipGMAPstate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_AipGMAPstate_Type.__name__=_C
_AipGMAPstate_Object=MibScalar
aipGMAPstate=_AipGMAPstate_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,1,1),_AipGMAPstate_Type())
aipGMAPstate.setMaxAccess(_E)
if mibBuilder.loadTexts:aipGMAPstate.setStatus(_B)
class _AipGMAPgaptime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AipGMAPgaptime_Type.__name__=_C
_AipGMAPgaptime_Object=MibScalar
aipGMAPgaptime=_AipGMAPgaptime_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,1,2),_AipGMAPgaptime_Type())
aipGMAPgaptime.setMaxAccess(_E)
if mibBuilder.loadTexts:aipGMAPgaptime.setStatus(_B)
class _AipGMAPupdatetime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AipGMAPupdatetime_Type.__name__=_C
_AipGMAPupdatetime_Object=MibScalar
aipGMAPupdatetime=_AipGMAPupdatetime_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,1,3),_AipGMAPupdatetime_Type())
aipGMAPupdatetime.setMaxAccess(_E)
if mibBuilder.loadTexts:aipGMAPupdatetime.setStatus(_B)
class _AipGMAPholdtime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AipGMAPholdtime_Type.__name__=_C
_AipGMAPholdtime_Object=MibScalar
aipGMAPholdtime=_AipGMAPholdtime_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,1,4),_AipGMAPholdtime_Type())
aipGMAPholdtime.setMaxAccess(_E)
if mibBuilder.loadTexts:aipGMAPholdtime.setStatus(_B)
class _AipGMAPLastTrapReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('authenticatedVlan',1),('conflictingBindingRule',2),('sameProtoDifferentVlansConflict',3),('sameVlanDifferentProtocolsConflict',4),('nonMobileVlan',5),('none',6)))
_AipGMAPLastTrapReason_Type.__name__=_C
_AipGMAPLastTrapReason_Object=MibScalar
aipGMAPLastTrapReason=_AipGMAPLastTrapReason_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,1,5),_AipGMAPLastTrapReason_Type())
aipGMAPLastTrapReason.setMaxAccess(_D)
if mibBuilder.loadTexts:aipGMAPLastTrapReason.setStatus(_B)
class _AipGMAPLastTrapPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AipGMAPLastTrapPort_Type.__name__=_C
_AipGMAPLastTrapPort_Object=MibScalar
aipGMAPLastTrapPort=_AipGMAPLastTrapPort_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,1,6),_AipGMAPLastTrapPort_Type())
aipGMAPLastTrapPort.setMaxAccess(_D)
if mibBuilder.loadTexts:aipGMAPLastTrapPort.setStatus(_B)
_AipGMAPLastTrapMac_Type=MacAddress
_AipGMAPLastTrapMac_Object=MibScalar
aipGMAPLastTrapMac=_AipGMAPLastTrapMac_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,1,7),_AipGMAPLastTrapMac_Type())
aipGMAPLastTrapMac.setMaxAccess(_D)
if mibBuilder.loadTexts:aipGMAPLastTrapMac.setStatus(_B)
class _AipGMAPLastTrapProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AipGMAPLastTrapProtocol_Type.__name__=_C
_AipGMAPLastTrapProtocol_Object=MibScalar
aipGMAPLastTrapProtocol=_AipGMAPLastTrapProtocol_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,1,8),_AipGMAPLastTrapProtocol_Type())
aipGMAPLastTrapProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:aipGMAPLastTrapProtocol.setStatus(_B)
class _AipGMAPLastTrapVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AipGMAPLastTrapVlan_Type.__name__=_C
_AipGMAPLastTrapVlan_Object=MibScalar
aipGMAPLastTrapVlan=_AipGMAPLastTrapVlan_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,1,9),_AipGMAPLastTrapVlan_Type())
aipGMAPLastTrapVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:aipGMAPLastTrapVlan.setStatus(_B)
_AipGMAPTable_Object=MibTable
aipGMAPTable=_AipGMAPTable_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,1,10))
if mibBuilder.loadTexts:aipGMAPTable.setStatus(_B)
_AipGMAPTableEntry_Object=MibTableRow
aipGMAPTableEntry=_AipGMAPTableEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,1,10,1))
aipGMAPTableEntry.setIndexNames((0,_A,_G),(0,_A,_H))
if mibBuilder.loadTexts:aipGMAPTableEntry.setStatus(_B)
_AipGMAPMacAddr_Type=MacAddress
_AipGMAPMacAddr_Object=MibTableColumn
aipGMAPMacAddr=_AipGMAPMacAddr_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,1,10,1,1),_AipGMAPMacAddr_Type())
aipGMAPMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:aipGMAPMacAddr.setStatus(_B)
_AipGMAPProtocol_Type=Unsigned32
_AipGMAPProtocol_Object=MibTableColumn
aipGMAPProtocol=_AipGMAPProtocol_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,1,10,1,2),_AipGMAPProtocol_Type())
aipGMAPProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:aipGMAPProtocol.setStatus(_B)
class _AipGMAPVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AipGMAPVlan_Type.__name__=_C
_AipGMAPVlan_Object=MibTableColumn
aipGMAPVlan=_AipGMAPVlan_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,1,10,1,3),_AipGMAPVlan_Type())
aipGMAPVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:aipGMAPVlan.setStatus(_B)
_AipGMAPSrcSwitch_Type=MacAddress
_AipGMAPSrcSwitch_Object=MibTableColumn
aipGMAPSrcSwitch=_AipGMAPSrcSwitch_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,1,10,1,4),_AipGMAPSrcSwitch_Type())
aipGMAPSrcSwitch.setMaxAccess(_D)
if mibBuilder.loadTexts:aipGMAPSrcSwitch.setStatus(_B)
class _AipGMAPFlags_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_AipGMAPFlags_Type.__name__=_U
_AipGMAPFlags_Object=MibTableColumn
aipGMAPFlags=_AipGMAPFlags_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,1,10,1,5),_AipGMAPFlags_Type())
aipGMAPFlags.setMaxAccess(_D)
if mibBuilder.loadTexts:aipGMAPFlags.setStatus(_B)
class _AipGMAPTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AipGMAPTimeout_Type.__name__=_C
_AipGMAPTimeout_Object=MibTableColumn
aipGMAPTimeout=_AipGMAPTimeout_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,1,10,1,6),_AipGMAPTimeout_Type())
aipGMAPTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:aipGMAPTimeout.setStatus(_B)
_AipAMAPconfig_ObjectIdentity=ObjectIdentity
aipAMAPconfig=_AipAMAPconfig_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,2))
class _AipAMAPstate_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_AipAMAPstate_Type.__name__=_C
_AipAMAPstate_Object=MibScalar
aipAMAPstate=_AipAMAPstate_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,2,1),_AipAMAPstate_Type())
aipAMAPstate.setMaxAccess(_E)
if mibBuilder.loadTexts:aipAMAPstate.setStatus(_B)
class _AipAMAPdisctime_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AipAMAPdisctime_Type.__name__=_C
_AipAMAPdisctime_Object=MibScalar
aipAMAPdisctime=_AipAMAPdisctime_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,2,2),_AipAMAPdisctime_Type())
aipAMAPdisctime.setMaxAccess(_E)
if mibBuilder.loadTexts:aipAMAPdisctime.setStatus(_B)
class _AipAMAPcommontime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AipAMAPcommontime_Type.__name__=_C
_AipAMAPcommontime_Object=MibScalar
aipAMAPcommontime=_AipAMAPcommontime_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,2,3),_AipAMAPcommontime_Type())
aipAMAPcommontime.setMaxAccess(_E)
if mibBuilder.loadTexts:aipAMAPcommontime.setStatus(_B)
class _AipAMAPLastTrapReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('add',1),('change',2),('remove',3),('none',4)))
_AipAMAPLastTrapReason_Type.__name__=_C
_AipAMAPLastTrapReason_Object=MibScalar
aipAMAPLastTrapReason=_AipAMAPLastTrapReason_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,2,4),_AipAMAPLastTrapReason_Type())
aipAMAPLastTrapReason.setMaxAccess(_D)
if mibBuilder.loadTexts:aipAMAPLastTrapReason.setStatus(_B)
class _AipAMAPLastTrapPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AipAMAPLastTrapPort_Type.__name__=_C
_AipAMAPLastTrapPort_Object=MibScalar
aipAMAPLastTrapPort=_AipAMAPLastTrapPort_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,2,5),_AipAMAPLastTrapPort_Type())
aipAMAPLastTrapPort.setMaxAccess(_D)
if mibBuilder.loadTexts:aipAMAPLastTrapPort.setStatus(_B)
_AipAMAPportConnectionTable_Object=MibTable
aipAMAPportConnectionTable=_AipAMAPportConnectionTable_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,2,6))
if mibBuilder.loadTexts:aipAMAPportConnectionTable.setStatus(_B)
_AipAMAPportConnectionentry_Object=MibTableRow
aipAMAPportConnectionentry=_AipAMAPportConnectionentry_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,2,6,1))
aipAMAPportConnectionentry.setIndexNames((0,_A,_I),(0,_A,_J),(0,_A,_K))
if mibBuilder.loadTexts:aipAMAPportConnectionentry.setStatus(_B)
class _AipAMAPLocalConnectionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AipAMAPLocalConnectionIndex_Type.__name__=_C
_AipAMAPLocalConnectionIndex_Object=MibTableColumn
aipAMAPLocalConnectionIndex=_AipAMAPLocalConnectionIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,2,6,1,1),_AipAMAPLocalConnectionIndex_Type())
aipAMAPLocalConnectionIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:aipAMAPLocalConnectionIndex.setStatus(_B)
_AipAMAPRemMac_Type=MacAddress
_AipAMAPRemMac_Object=MibTableColumn
aipAMAPRemMac=_AipAMAPRemMac_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,2,6,1,2),_AipAMAPRemMac_Type())
aipAMAPRemMac.setMaxAccess(_D)
if mibBuilder.loadTexts:aipAMAPRemMac.setStatus(_B)
class _AipAMAPRemConnectionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AipAMAPRemConnectionIndex_Type.__name__=_C
_AipAMAPRemConnectionIndex_Object=MibTableColumn
aipAMAPRemConnectionIndex=_AipAMAPRemConnectionIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,2,6,1,3),_AipAMAPRemConnectionIndex_Type())
aipAMAPRemConnectionIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:aipAMAPRemConnectionIndex.setStatus(_B)
class _AipAMAPRemVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AipAMAPRemVlan_Type.__name__=_C
_AipAMAPRemVlan_Object=MibTableColumn
aipAMAPRemVlan=_AipAMAPRemVlan_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,2,6,1,4),_AipAMAPRemVlan_Type())
aipAMAPRemVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:aipAMAPRemVlan.setStatus(_B)
class _AipAMAPRemHostname_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AipAMAPRemHostname_Type.__name__=_F
_AipAMAPRemHostname_Object=MibTableColumn
aipAMAPRemHostname=_AipAMAPRemHostname_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,2,6,1,5),_AipAMAPRemHostname_Type())
aipAMAPRemHostname.setMaxAccess(_D)
if mibBuilder.loadTexts:aipAMAPRemHostname.setStatus(_B)
_AipAMAPLocalIfindex_Type=InterfaceIndex
_AipAMAPLocalIfindex_Object=MibTableColumn
aipAMAPLocalIfindex=_AipAMAPLocalIfindex_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,2,6,1,6),_AipAMAPLocalIfindex_Type())
aipAMAPLocalIfindex.setMaxAccess(_D)
if mibBuilder.loadTexts:aipAMAPLocalIfindex.setStatus(_B)
class _AipAMAPLocalSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AipAMAPLocalSlot_Type.__name__=_C
_AipAMAPLocalSlot_Object=MibTableColumn
aipAMAPLocalSlot=_AipAMAPLocalSlot_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,2,6,1,7),_AipAMAPLocalSlot_Type())
aipAMAPLocalSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:aipAMAPLocalSlot.setStatus(_B)
class _AipAMAPLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AipAMAPLocalPort_Type.__name__=_C
_AipAMAPLocalPort_Object=MibTableColumn
aipAMAPLocalPort=_AipAMAPLocalPort_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,2,6,1,8),_AipAMAPLocalPort_Type())
aipAMAPLocalPort.setMaxAccess(_D)
if mibBuilder.loadTexts:aipAMAPLocalPort.setStatus(_B)
class _AipAMAPRemSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AipAMAPRemSlot_Type.__name__=_C
_AipAMAPRemSlot_Object=MibTableColumn
aipAMAPRemSlot=_AipAMAPRemSlot_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,2,6,1,9),_AipAMAPRemSlot_Type())
aipAMAPRemSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:aipAMAPRemSlot.setStatus(_B)
class _AipAMAPRemPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AipAMAPRemPort_Type.__name__=_C
_AipAMAPRemPort_Object=MibTableColumn
aipAMAPRemPort=_AipAMAPRemPort_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,2,6,1,10),_AipAMAPRemPort_Type())
aipAMAPRemPort.setMaxAccess(_D)
if mibBuilder.loadTexts:aipAMAPRemPort.setStatus(_B)
class _AipAMAPRemDeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,10,20,21,22,23,24,30,31,32,34,35,36,40,41,42,43,44,50,51,52,53,54,55,56,57,60,61,62,70,71,72,73,74,75,76,77,78,79,80,81,82,87,88,89,90,91,92,93,94,95,96,97,98,214,215,216,217,218,219,220,221,222,223,227,249,250,251,252,253,254,255)));namedValues=NamedValues(*(('unknownDevice',1),('omniSwitch7700',2),('omniSwitch7800',3),('omniSwitch9600',4),('omniSwitch9700',5),('omniSwitch9800',6),('omniSwitch8800',10),('omniSwitch6624',20),('omniSwitch6648',21),('omniSwitch6624Fiber',22),('omniSwitch6624Ver2',23),('omniSwitch6648Ver2',24),('omniSwitch6824',30),('omniSwitch6848',31),('omniSwitch6824Fiber',32),('omniSwitch6850-24',34),('omniSwitch6850-48',35),('omniSwitch6850-24Fiber',36),('omniSwitch5slotXOS',40),('omniSwitch9slotXOS',41),('omniSwitchRouterXOS',42),('omniAccess408',43),('omniAccess512',44),('omniStack2032',50),('omniStack4024',51),('omniStack5024',52),('omniStack6024',53),('omniStack6048',54),('omniStack6124',55),('omniStack6148',56),('omniStack8008',57),('omniAccess210',60),('omniAccess250',61),('omniAccess280',62),(_Y,70),('omniPCX4400',71),('omniSwitch6855-14',72),('omniSwitch6855-U10',73),('omniSwitch6855-24',74),('omniSwitch6855-U24',75),('omniSwitch6424',76),('omniSwitch6448',77),('omniSwitch6424Fiber',78),('omniSwitch6855-U24X',79),('omniSwitch62508ME',80),('omniSwitch625024ME',81),('omniSwitch625024SMB',82),('omniSwitch645010',87),('omniSwitch6450645024',88),('omniSwitch6450645024U',89),('omniSwitch645048',90),('omniSwitch6250U24M',91),('omniSwitch645024SF',92),('omniSwitch645048SF',93),('omniSwitch6450S10',94),('omniSwitch635024',95),('omniSwitch6350P24',96),('omniSwitch635048',97),('omniSwitch6350P48',98),('omniSwitch6200-MIXED-STACK',214),('omniSwitch6224',215),('omniSwitch6224P',216),('omniSwitch6248',217),('omniSwitch6248P',218),('omniSwitch6224-DC',219),('omniSwitch6248-DC',220),('omniSwitch6212',221),('omniSwitch6212P',222),('omniSwitch6224U',223),('omniSwitch6324',227),('omniAccess5000',249),('omniAccess4324',250),('omniAccess4308',251),('omniAccess6000',252),('omniAccessAP60',253),('omniAccessAP61',254),('omniAccessAP70',255)))
_AipAMAPRemDeviceType_Type.__name__=_C
_AipAMAPRemDeviceType_Object=MibTableColumn
aipAMAPRemDeviceType=_AipAMAPRemDeviceType_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,2,6,1,11),_AipAMAPRemDeviceType_Type())
aipAMAPRemDeviceType.setMaxAccess(_D)
if mibBuilder.loadTexts:aipAMAPRemDeviceType.setStatus(_B)
class _AipAMAPRemDevModelName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AipAMAPRemDevModelName_Type.__name__=_F
_AipAMAPRemDevModelName_Object=MibTableColumn
aipAMAPRemDevModelName=_AipAMAPRemDevModelName_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,2,6,1,12),_AipAMAPRemDevModelName_Type())
aipAMAPRemDevModelName.setMaxAccess(_D)
if mibBuilder.loadTexts:aipAMAPRemDevModelName.setStatus(_B)
class _AipAMAPRemProductType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('unknown',0),('chassis',1),('stack',2),('accessPoint',3),('pcx',4),(_Y,5),('standAlone',6)))
_AipAMAPRemProductType_Type.__name__=_C
_AipAMAPRemProductType_Object=MibTableColumn
aipAMAPRemProductType=_AipAMAPRemProductType_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,2,6,1,13),_AipAMAPRemProductType_Type())
aipAMAPRemProductType.setMaxAccess(_D)
if mibBuilder.loadTexts:aipAMAPRemProductType.setStatus(_B)
_AipAMAPhostsTable_Object=MibTable
aipAMAPhostsTable=_AipAMAPhostsTable_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,2,7))
if mibBuilder.loadTexts:aipAMAPhostsTable.setStatus(_B)
_AipAMAPHostentry_Object=MibTableRow
aipAMAPHostentry=_AipAMAPHostentry_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,2,7,1))
aipAMAPHostentry.setIndexNames((0,_A,_L),(0,_A,_M))
if mibBuilder.loadTexts:aipAMAPHostentry.setStatus(_B)
_AipAMAPHostMac_Type=MacAddress
_AipAMAPHostMac_Object=MibTableColumn
aipAMAPHostMac=_AipAMAPHostMac_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,2,7,1,1),_AipAMAPHostMac_Type())
aipAMAPHostMac.setMaxAccess(_D)
if mibBuilder.loadTexts:aipAMAPHostMac.setStatus(_B)
_AipAMAPIpAddr_Type=IpAddress
_AipAMAPIpAddr_Object=MibTableColumn
aipAMAPIpAddr=_AipAMAPIpAddr_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,2,7,1,2),_AipAMAPIpAddr_Type())
aipAMAPIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:aipAMAPIpAddr.setStatus(_B)
class _AipAMAPVoiceVlan_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_AipAMAPVoiceVlan_Type.__name__=_C
_AipAMAPVoiceVlan_Object=MibScalar
aipAMAPVoiceVlan=_AipAMAPVoiceVlan_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,2,8),_AipAMAPVoiceVlan_Type())
aipAMAPVoiceVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:aipAMAPVoiceVlan.setStatus(_B)
class _AipAMAPportstatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AipAMAPportstatus_Type.__name__=_C
_AipAMAPportstatus_Object=MibScalar
aipAMAPportstatus=_AipAMAPportstatus_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,2,10),_AipAMAPportstatus_Type())
aipAMAPportstatus.setMaxAccess(_E)
if mibBuilder.loadTexts:aipAMAPportstatus.setStatus(_B)
_AipLLDPConfig_ObjectIdentity=ObjectIdentity
aipLLDPConfig=_AipLLDPConfig_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,3))
_AipLLDPConfigManAddrTable_Object=MibTable
aipLLDPConfigManAddrTable=_AipLLDPConfigManAddrTable_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,3,1))
if mibBuilder.loadTexts:aipLLDPConfigManAddrTable.setStatus(_B)
_AipLLDPConfigManAddrEntry_Object=MibTableRow
aipLLDPConfigManAddrEntry=_AipLLDPConfigManAddrEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,3,1,1))
aipLLDPConfigManAddrEntry.setIndexNames((0,_A,_Z))
if mibBuilder.loadTexts:aipLLDPConfigManAddrEntry.setStatus(_B)
_AipLLDPConfigManAddrPortNum_Type=InterfaceIndex
_AipLLDPConfigManAddrPortNum_Object=MibTableColumn
aipLLDPConfigManAddrPortNum=_AipLLDPConfigManAddrPortNum_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,3,1,1,1),_AipLLDPConfigManAddrPortNum_Type())
aipLLDPConfigManAddrPortNum.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:aipLLDPConfigManAddrPortNum.setStatus(_B)
class _AipLLDPConfigManAddrTlvTxEnable_Type(TruthValue):defaultValue=2
_AipLLDPConfigManAddrTlvTxEnable_Type.__name__=_V
_AipLLDPConfigManAddrTlvTxEnable_Object=MibTableColumn
aipLLDPConfigManAddrTlvTxEnable=_AipLLDPConfigManAddrTlvTxEnable_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,3,1,1,2),_AipLLDPConfigManAddrTlvTxEnable_Type())
aipLLDPConfigManAddrTlvTxEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:aipLLDPConfigManAddrTlvTxEnable.setStatus(_B)
class _AipLLDPDestMac_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nearestBridge',1),('nearestEdge',2)))
_AipLLDPDestMac_Type.__name__=_C
_AipLLDPDestMac_Object=MibScalar
aipLLDPDestMac=_AipLLDPDestMac_Object((1,3,6,1,4,1,6486,800,1,2,1,9,1,1,3,2),_AipLLDPDestMac_Type())
aipLLDPDestMac.setMaxAccess(_E)
if mibBuilder.loadTexts:aipLLDPDestMac.setStatus(_B)
_AlcatelIND1InterswitchProtocolMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1InterswitchProtocolMIBConformance=_AlcatelIND1InterswitchProtocolMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,9,1,2))
_AlcatelIND1InterswitchProtocolMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1InterswitchProtocolMIBGroups=_AlcatelIND1InterswitchProtocolMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,9,1,2,1))
_AlcatelIND1InterswitchProtocolMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1InterswitchProtocolMIBCompliances=_AlcatelIND1InterswitchProtocolMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,9,1,2,2))
aipGMAPConfGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,9,1,2,1,1))
aipGMAPConfGroup.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_G),(_A,_H),(_A,_e),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:aipGMAPConfGroup.setStatus(_B)
aipAMAPConfGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,9,1,2,1,2))
aipAMAPConfGroup.setObjects(*((_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_S),(_A,_T),(_A,_I),(_A,_J),(_A,_K),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:aipAMAPConfGroup.setStatus(_B)
aipLLDPConfGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,9,1,2,1,4))
aipLLDPConfGroup.setObjects((_A,_u))
if mibBuilder.loadTexts:aipLLDPConfGroup.setStatus(_B)
aipLLDPConfigManAddrEntryGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,9,1,2,1,5))
aipLLDPConfigManAddrEntryGroup.setObjects((_A,_v))
if mibBuilder.loadTexts:aipLLDPConfigManAddrEntryGroup.setStatus(_B)
aipAMAPStatusTrap=NotificationType((1,3,6,1,4,1,6486,800,1,3,2,1,0,1))
aipAMAPStatusTrap.setObjects(*((_A,_S),(_A,_T)))
if mibBuilder.loadTexts:aipAMAPStatusTrap.setStatus(_B)
aipGMAPConflictTrap=NotificationType((1,3,6,1,4,1,6486,800,1,3,2,2,0,1))
aipGMAPConflictTrap.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:aipGMAPConflictTrap.setStatus(_B)
aipNotificationGroup=NotificationGroup((1,3,6,1,4,1,6486,800,1,2,1,9,1,2,1,3))
aipNotificationGroup.setObjects(*((_A,_w),(_A,_x)))
if mibBuilder.loadTexts:aipNotificationGroup.setStatus(_B)
alcatelIND1InterswitchProtocolMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,9,1,2,2,1))
alcatelIND1InterswitchProtocolMIBCompliance.setObjects(*((_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:alcatelIND1InterswitchProtocolMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'alcatelIND1InterswitchProtocolMIB':alcatelIND1InterswitchProtocolMIB,'alcatelIND1InterswitchProtocolMIBObjects':alcatelIND1InterswitchProtocolMIBObjects,'aipGMAPconfig':aipGMAPconfig,_a:aipGMAPstate,_b:aipGMAPgaptime,_c:aipGMAPupdatetime,_d:aipGMAPholdtime,_N:aipGMAPLastTrapReason,_O:aipGMAPLastTrapPort,_P:aipGMAPLastTrapMac,_Q:aipGMAPLastTrapProtocol,_R:aipGMAPLastTrapVlan,'aipGMAPTable':aipGMAPTable,'aipGMAPTableEntry':aipGMAPTableEntry,_G:aipGMAPMacAddr,_H:aipGMAPProtocol,_e:aipGMAPVlan,_f:aipGMAPSrcSwitch,_g:aipGMAPFlags,_h:aipGMAPTimeout,'aipAMAPconfig':aipAMAPconfig,_i:aipAMAPstate,_j:aipAMAPdisctime,_k:aipAMAPcommontime,_S:aipAMAPLastTrapReason,_T:aipAMAPLastTrapPort,'aipAMAPportConnectionTable':aipAMAPportConnectionTable,'aipAMAPportConnectionentry':aipAMAPportConnectionentry,_I:aipAMAPLocalConnectionIndex,_J:aipAMAPRemMac,_K:aipAMAPRemConnectionIndex,_m:aipAMAPRemVlan,_n:aipAMAPRemHostname,_p:aipAMAPLocalIfindex,_q:aipAMAPLocalSlot,_r:aipAMAPLocalPort,_s:aipAMAPRemSlot,_t:aipAMAPRemPort,'aipAMAPRemDeviceType':aipAMAPRemDeviceType,'aipAMAPRemDevModelName':aipAMAPRemDevModelName,'aipAMAPRemProductType':aipAMAPRemProductType,'aipAMAPhostsTable':aipAMAPhostsTable,'aipAMAPHostentry':aipAMAPHostentry,_L:aipAMAPHostMac,_M:aipAMAPIpAddr,_o:aipAMAPVoiceVlan,_l:aipAMAPportstatus,'aipLLDPConfig':aipLLDPConfig,'aipLLDPConfigManAddrTable':aipLLDPConfigManAddrTable,'aipLLDPConfigManAddrEntry':aipLLDPConfigManAddrEntry,_Z:aipLLDPConfigManAddrPortNum,_v:aipLLDPConfigManAddrTlvTxEnable,_u:aipLLDPDestMac,'alcatelIND1InterswitchProtocolMIBConformance':alcatelIND1InterswitchProtocolMIBConformance,'alcatelIND1InterswitchProtocolMIBGroups':alcatelIND1InterswitchProtocolMIBGroups,_y:aipGMAPConfGroup,_z:aipAMAPConfGroup,_A0:aipNotificationGroup,_A1:aipLLDPConfGroup,_A2:aipLLDPConfigManAddrEntryGroup,'alcatelIND1InterswitchProtocolMIBCompliances':alcatelIND1InterswitchProtocolMIBCompliances,'alcatelIND1InterswitchProtocolMIBCompliance':alcatelIND1InterswitchProtocolMIBCompliance,_w:aipAMAPStatusTrap,_x:aipGMAPConflictTrap})