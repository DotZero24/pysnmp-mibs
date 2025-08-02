_W='multicastclient'
_V='broadcastclient'
_U='reservedPrivate'
_T='reservedControl'
_S='broadcast'
_R='server'
_Q='client'
_P='symmetricPassive'
_O='symmetricActive'
_N='unspecified'
_M='not-accessible'
_L='hpnicfNTPPeerHMode'
_K='hpnicfNTPPeerRemAdr'
_J='subtractSecond'
_I='addSecond'
_H='noWarning'
_G='HPN-ICF-NTP-MIB'
_F='read-write'
_E='Unsigned32'
_D='Integer32'
_C='OctetString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfRhw,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfRhw')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
hpnicfNTP=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,8,22))
if mibBuilder.loadTexts:hpnicfNTP.setRevisions(('2003-03-15 00:00',))
_HpnicfNTPSystemMIB_ObjectIdentity=ObjectIdentity
hpnicfNTPSystemMIB=_HpnicfNTPSystemMIB_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,22,1))
_HpnicfNTPSystemMIBObjects_ObjectIdentity=ObjectIdentity
hpnicfNTPSystemMIBObjects=_HpnicfNTPSystemMIBObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,22,1,1))
class _HpnicfNTPSysLeap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_H,0),(_I,1),(_J,2),('alarm',3)))
_HpnicfNTPSysLeap_Type.__name__=_D
_HpnicfNTPSysLeap_Object=MibScalar
hpnicfNTPSysLeap=_HpnicfNTPSysLeap_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,1,1,1),_HpnicfNTPSysLeap_Type())
hpnicfNTPSysLeap.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPSysLeap.setStatus(_A)
class _HpnicfNTPSysStratum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HpnicfNTPSysStratum_Type.__name__=_D
_HpnicfNTPSysStratum_Object=MibScalar
hpnicfNTPSysStratum=_HpnicfNTPSysStratum_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,1,1,2),_HpnicfNTPSysStratum_Type())
hpnicfNTPSysStratum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPSysStratum.setStatus(_A)
class _HpnicfNTPSysPrecision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-20,20))
_HpnicfNTPSysPrecision_Type.__name__=_D
_HpnicfNTPSysPrecision_Object=MibScalar
hpnicfNTPSysPrecision=_HpnicfNTPSysPrecision_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,1,1,3),_HpnicfNTPSysPrecision_Type())
hpnicfNTPSysPrecision.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPSysPrecision.setStatus(_A)
class _HpnicfNTPSysRootdelay_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HpnicfNTPSysRootdelay_Type.__name__=_C
_HpnicfNTPSysRootdelay_Object=MibScalar
hpnicfNTPSysRootdelay=_HpnicfNTPSysRootdelay_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,1,1,4),_HpnicfNTPSysRootdelay_Type())
hpnicfNTPSysRootdelay.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPSysRootdelay.setStatus(_A)
class _HpnicfNTPSysRootdispersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HpnicfNTPSysRootdispersion_Type.__name__=_C
_HpnicfNTPSysRootdispersion_Object=MibScalar
hpnicfNTPSysRootdispersion=_HpnicfNTPSysRootdispersion_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,1,1,5),_HpnicfNTPSysRootdispersion_Type())
hpnicfNTPSysRootdispersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPSysRootdispersion.setStatus(_A)
class _HpnicfNTPSysRefid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HpnicfNTPSysRefid_Type.__name__=_C
_HpnicfNTPSysRefid_Object=MibScalar
hpnicfNTPSysRefid=_HpnicfNTPSysRefid_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,1,1,6),_HpnicfNTPSysRefid_Type())
hpnicfNTPSysRefid.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPSysRefid.setStatus(_A)
class _HpnicfNTPSysReftime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HpnicfNTPSysReftime_Type.__name__=_C
_HpnicfNTPSysReftime_Object=MibScalar
hpnicfNTPSysReftime=_HpnicfNTPSysReftime_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,1,1,7),_HpnicfNTPSysReftime_Type())
hpnicfNTPSysReftime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPSysReftime.setStatus(_A)
class _HpnicfNTPSysPoll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-20,20))
_HpnicfNTPSysPoll_Type.__name__=_D
_HpnicfNTPSysPoll_Object=MibScalar
hpnicfNTPSysPoll=_HpnicfNTPSysPoll_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,1,1,8),_HpnicfNTPSysPoll_Type())
hpnicfNTPSysPoll.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPSysPoll.setStatus(_A)
class _HpnicfNTPSysPeer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfNTPSysPeer_Type.__name__=_D
_HpnicfNTPSysPeer_Object=MibScalar
hpnicfNTPSysPeer=_HpnicfNTPSysPeer_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,1,1,9),_HpnicfNTPSysPeer_Type())
hpnicfNTPSysPeer.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPSysPeer.setStatus('obsolete')
class _HpnicfNTPSysState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('noUpdateClock',0),('getfreqInfo',1),('clockBySet',2),('clockBySetAndNoFreq',3),('clockBySyns',4),('findError',5)))
_HpnicfNTPSysState_Type.__name__=_D
_HpnicfNTPSysState_Object=MibScalar
hpnicfNTPSysState=_HpnicfNTPSysState_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,1,1,10),_HpnicfNTPSysState_Type())
hpnicfNTPSysState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPSysState.setStatus(_A)
class _HpnicfNTPSysOffset_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HpnicfNTPSysOffset_Type.__name__=_C
_HpnicfNTPSysOffset_Object=MibScalar
hpnicfNTPSysOffset=_HpnicfNTPSysOffset_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,1,1,11),_HpnicfNTPSysOffset_Type())
hpnicfNTPSysOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPSysOffset.setStatus(_A)
class _HpnicfNTPSysDrift_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HpnicfNTPSysDrift_Type.__name__=_C
_HpnicfNTPSysDrift_Object=MibScalar
hpnicfNTPSysDrift=_HpnicfNTPSysDrift_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,1,1,12),_HpnicfNTPSysDrift_Type())
hpnicfNTPSysDrift.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPSysDrift.setStatus(_A)
class _HpnicfNTPSysCompliance_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HpnicfNTPSysCompliance_Type.__name__=_C
_HpnicfNTPSysCompliance_Object=MibScalar
hpnicfNTPSysCompliance=_HpnicfNTPSysCompliance_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,1,1,13),_HpnicfNTPSysCompliance_Type())
hpnicfNTPSysCompliance.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPSysCompliance.setStatus(_A)
class _HpnicfNTPSysClock_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HpnicfNTPSysClock_Type.__name__=_C
_HpnicfNTPSysClock_Object=MibScalar
hpnicfNTPSysClock=_HpnicfNTPSysClock_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,1,1,14),_HpnicfNTPSysClock_Type())
hpnicfNTPSysClock.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPSysClock.setStatus(_A)
class _HpnicfNTPSysStabil_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HpnicfNTPSysStabil_Type.__name__=_C
_HpnicfNTPSysStabil_Object=MibScalar
hpnicfNTPSysStabil=_HpnicfNTPSysStabil_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,1,1,15),_HpnicfNTPSysStabil_Type())
hpnicfNTPSysStabil.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPSysStabil.setStatus(_A)
class _HpnicfNTPSysAuthenticate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noAuthenticate',0),('authenticate',1)))
_HpnicfNTPSysAuthenticate_Type.__name__=_D
_HpnicfNTPSysAuthenticate_Object=MibScalar
hpnicfNTPSysAuthenticate=_HpnicfNTPSysAuthenticate_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,1,1,16),_HpnicfNTPSysAuthenticate_Type())
hpnicfNTPSysAuthenticate.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNTPSysAuthenticate.setStatus(_A)
class _HpnicfNTPSysPollSec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,1048576))
_HpnicfNTPSysPollSec_Type.__name__=_D
_HpnicfNTPSysPollSec_Object=MibScalar
hpnicfNTPSysPollSec=_HpnicfNTPSysPollSec_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,1,1,17),_HpnicfNTPSysPollSec_Type())
hpnicfNTPSysPollSec.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNTPSysPollSec.setStatus(_A)
_HpnicfNTPSysClockSec_Type=Integer32
_HpnicfNTPSysClockSec_Object=MibScalar
hpnicfNTPSysClockSec=_HpnicfNTPSysClockSec_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,1,1,18),_HpnicfNTPSysClockSec_Type())
hpnicfNTPSysClockSec.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPSysClockSec.setStatus(_A)
_HpnicfNTPServerIP_Type=IpAddress
_HpnicfNTPServerIP_Object=MibScalar
hpnicfNTPServerIP=_HpnicfNTPServerIP_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,1,1,19),_HpnicfNTPServerIP_Type())
hpnicfNTPServerIP.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNTPServerIP.setStatus(_A)
class _HpnicfNTPSysSrcPeer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HpnicfNTPSysSrcPeer_Type.__name__=_E
_HpnicfNTPSysSrcPeer_Object=MibScalar
hpnicfNTPSysSrcPeer=_HpnicfNTPSysSrcPeer_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,1,1,20),_HpnicfNTPSysSrcPeer_Type())
hpnicfNTPSysSrcPeer.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPSysSrcPeer.setStatus(_A)
_HpnicfNTPPeerMIB_ObjectIdentity=ObjectIdentity
hpnicfNTPPeerMIB=_HpnicfNTPPeerMIB_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,22,2))
_HpnicfNTPPeerMIBObjects_ObjectIdentity=ObjectIdentity
hpnicfNTPPeerMIBObjects=_HpnicfNTPPeerMIBObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1))
_HpnicfNTPPeerTable_Object=MibTable
hpnicfNTPPeerTable=_HpnicfNTPPeerTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1))
if mibBuilder.loadTexts:hpnicfNTPPeerTable.setStatus(_A)
_HpnicfNTPPeerEntry_Object=MibTableRow
hpnicfNTPPeerEntry=_HpnicfNTPPeerEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1))
hpnicfNTPPeerEntry.setIndexNames((0,_G,_K),(0,_G,_L))
if mibBuilder.loadTexts:hpnicfNTPPeerEntry.setStatus(_A)
_HpnicfNTPPeerConfig_Type=TruthValue
_HpnicfNTPPeerConfig_Object=MibTableColumn
hpnicfNTPPeerConfig=_HpnicfNTPPeerConfig_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,1),_HpnicfNTPPeerConfig_Type())
hpnicfNTPPeerConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerConfig.setStatus(_A)
_HpnicfNTPPeerAuthenable_Type=TruthValue
_HpnicfNTPPeerAuthenable_Object=MibTableColumn
hpnicfNTPPeerAuthenable=_HpnicfNTPPeerAuthenable_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,2),_HpnicfNTPPeerAuthenable_Type())
hpnicfNTPPeerAuthenable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerAuthenable.setStatus(_A)
_HpnicfNTPPeerAuthentic_Type=TruthValue
_HpnicfNTPPeerAuthentic_Object=MibTableColumn
hpnicfNTPPeerAuthentic=_HpnicfNTPPeerAuthentic_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,3),_HpnicfNTPPeerAuthentic_Type())
hpnicfNTPPeerAuthentic.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerAuthentic.setStatus(_A)
_HpnicfNTPPeerRemAdr_Type=IpAddress
_HpnicfNTPPeerRemAdr_Object=MibTableColumn
hpnicfNTPPeerRemAdr=_HpnicfNTPPeerRemAdr_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,4),_HpnicfNTPPeerRemAdr_Type())
hpnicfNTPPeerRemAdr.setMaxAccess(_M)
if mibBuilder.loadTexts:hpnicfNTPPeerRemAdr.setStatus(_A)
class _HpnicfNTPPeerRemPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfNTPPeerRemPort_Type.__name__=_D
_HpnicfNTPPeerRemPort_Object=MibTableColumn
hpnicfNTPPeerRemPort=_HpnicfNTPPeerRemPort_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,5),_HpnicfNTPPeerRemPort_Type())
hpnicfNTPPeerRemPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerRemPort.setStatus(_A)
_HpnicfNTPPeerLocAdr_Type=IpAddress
_HpnicfNTPPeerLocAdr_Object=MibTableColumn
hpnicfNTPPeerLocAdr=_HpnicfNTPPeerLocAdr_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,6),_HpnicfNTPPeerLocAdr_Type())
hpnicfNTPPeerLocAdr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerLocAdr.setStatus(_A)
class _HpnicfNTPPeerLocPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfNTPPeerLocPort_Type.__name__=_D
_HpnicfNTPPeerLocPort_Object=MibTableColumn
hpnicfNTPPeerLocPort=_HpnicfNTPPeerLocPort_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,7),_HpnicfNTPPeerLocPort_Type())
hpnicfNTPPeerLocPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerLocPort.setStatus(_A)
class _HpnicfNTPPeerLeap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_H,0),(_I,1),(_J,2),('alarm',3)))
_HpnicfNTPPeerLeap_Type.__name__=_D
_HpnicfNTPPeerLeap_Object=MibTableColumn
hpnicfNTPPeerLeap=_HpnicfNTPPeerLeap_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,8),_HpnicfNTPPeerLeap_Type())
hpnicfNTPPeerLeap.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerLeap.setStatus(_A)
class _HpnicfNTPPeerHMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_N,0),(_O,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),(_V,8),(_W,9)))
_HpnicfNTPPeerHMode_Type.__name__=_D
_HpnicfNTPPeerHMode_Object=MibTableColumn
hpnicfNTPPeerHMode=_HpnicfNTPPeerHMode_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,9),_HpnicfNTPPeerHMode_Type())
hpnicfNTPPeerHMode.setMaxAccess(_M)
if mibBuilder.loadTexts:hpnicfNTPPeerHMode.setStatus(_A)
class _HpnicfNTPPeerStratum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnicfNTPPeerStratum_Type.__name__=_D
_HpnicfNTPPeerStratum_Object=MibTableColumn
hpnicfNTPPeerStratum=_HpnicfNTPPeerStratum_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,10),_HpnicfNTPPeerStratum_Type())
hpnicfNTPPeerStratum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerStratum.setStatus(_A)
class _HpnicfNTPPeerPPoll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-20,20))
_HpnicfNTPPeerPPoll_Type.__name__=_D
_HpnicfNTPPeerPPoll_Object=MibTableColumn
hpnicfNTPPeerPPoll=_HpnicfNTPPeerPPoll_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,11),_HpnicfNTPPeerPPoll_Type())
hpnicfNTPPeerPPoll.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerPPoll.setStatus(_A)
class _HpnicfNTPPeerHPoll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-20,20))
_HpnicfNTPPeerHPoll_Type.__name__=_D
_HpnicfNTPPeerHPoll_Object=MibTableColumn
hpnicfNTPPeerHPoll=_HpnicfNTPPeerHPoll_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,12),_HpnicfNTPPeerHPoll_Type())
hpnicfNTPPeerHPoll.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerHPoll.setStatus(_A)
class _HpnicfNTPPeerPrecision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-20,20))
_HpnicfNTPPeerPrecision_Type.__name__=_D
_HpnicfNTPPeerPrecision_Object=MibTableColumn
hpnicfNTPPeerPrecision=_HpnicfNTPPeerPrecision_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,13),_HpnicfNTPPeerPrecision_Type())
hpnicfNTPPeerPrecision.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerPrecision.setStatus(_A)
class _HpnicfNTPPeerRootDelay_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HpnicfNTPPeerRootDelay_Type.__name__=_C
_HpnicfNTPPeerRootDelay_Object=MibTableColumn
hpnicfNTPPeerRootDelay=_HpnicfNTPPeerRootDelay_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,14),_HpnicfNTPPeerRootDelay_Type())
hpnicfNTPPeerRootDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerRootDelay.setStatus(_A)
class _HpnicfNTPPeerRootDispersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HpnicfNTPPeerRootDispersion_Type.__name__=_C
_HpnicfNTPPeerRootDispersion_Object=MibTableColumn
hpnicfNTPPeerRootDispersion=_HpnicfNTPPeerRootDispersion_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,15),_HpnicfNTPPeerRootDispersion_Type())
hpnicfNTPPeerRootDispersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerRootDispersion.setStatus(_A)
class _HpnicfNTPPeerRefId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HpnicfNTPPeerRefId_Type.__name__=_C
_HpnicfNTPPeerRefId_Object=MibTableColumn
hpnicfNTPPeerRefId=_HpnicfNTPPeerRefId_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,16),_HpnicfNTPPeerRefId_Type())
hpnicfNTPPeerRefId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerRefId.setStatus(_A)
class _HpnicfNTPPeerRefTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HpnicfNTPPeerRefTime_Type.__name__=_C
_HpnicfNTPPeerRefTime_Object=MibTableColumn
hpnicfNTPPeerRefTime=_HpnicfNTPPeerRefTime_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,17),_HpnicfNTPPeerRefTime_Type())
hpnicfNTPPeerRefTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerRefTime.setStatus(_A)
class _HpnicfNTPPeerOrg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HpnicfNTPPeerOrg_Type.__name__=_C
_HpnicfNTPPeerOrg_Object=MibTableColumn
hpnicfNTPPeerOrg=_HpnicfNTPPeerOrg_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,18),_HpnicfNTPPeerOrg_Type())
hpnicfNTPPeerOrg.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerOrg.setStatus(_A)
class _HpnicfNTPPeerRec_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HpnicfNTPPeerRec_Type.__name__=_C
_HpnicfNTPPeerRec_Object=MibTableColumn
hpnicfNTPPeerRec=_HpnicfNTPPeerRec_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,19),_HpnicfNTPPeerRec_Type())
hpnicfNTPPeerRec.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerRec.setStatus(_A)
class _HpnicfNTPPeerXmt_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HpnicfNTPPeerXmt_Type.__name__=_C
_HpnicfNTPPeerXmt_Object=MibTableColumn
hpnicfNTPPeerXmt=_HpnicfNTPPeerXmt_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,20),_HpnicfNTPPeerXmt_Type())
hpnicfNTPPeerXmt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerXmt.setStatus(_A)
class _HpnicfNTPPeerReach_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfNTPPeerReach_Type.__name__=_D
_HpnicfNTPPeerReach_Object=MibTableColumn
hpnicfNTPPeerReach=_HpnicfNTPPeerReach_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,21),_HpnicfNTPPeerReach_Type())
hpnicfNTPPeerReach.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerReach.setStatus(_A)
class _HpnicfNTPPeerValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnicfNTPPeerValid_Type.__name__=_D
_HpnicfNTPPeerValid_Object=MibTableColumn
hpnicfNTPPeerValid=_HpnicfNTPPeerValid_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,22),_HpnicfNTPPeerValid_Type())
hpnicfNTPPeerValid.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerValid.setStatus(_A)
class _HpnicfNTPPeerTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfNTPPeerTimer_Type.__name__=_D
_HpnicfNTPPeerTimer_Object=MibTableColumn
hpnicfNTPPeerTimer=_HpnicfNTPPeerTimer_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,23),_HpnicfNTPPeerTimer_Type())
hpnicfNTPPeerTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerTimer.setStatus(_A)
class _HpnicfNTPPeerDelay_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HpnicfNTPPeerDelay_Type.__name__=_C
_HpnicfNTPPeerDelay_Object=MibTableColumn
hpnicfNTPPeerDelay=_HpnicfNTPPeerDelay_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,24),_HpnicfNTPPeerDelay_Type())
hpnicfNTPPeerDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerDelay.setStatus(_A)
class _HpnicfNTPPeerOffset_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HpnicfNTPPeerOffset_Type.__name__=_C
_HpnicfNTPPeerOffset_Object=MibTableColumn
hpnicfNTPPeerOffset=_HpnicfNTPPeerOffset_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,25),_HpnicfNTPPeerOffset_Type())
hpnicfNTPPeerOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerOffset.setStatus(_A)
class _HpnicfNTPPeerJitter_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HpnicfNTPPeerJitter_Type.__name__=_C
_HpnicfNTPPeerJitter_Object=MibTableColumn
hpnicfNTPPeerJitter=_HpnicfNTPPeerJitter_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,26),_HpnicfNTPPeerJitter_Type())
hpnicfNTPPeerJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerJitter.setStatus(_A)
class _HpnicfNTPPeerDispersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HpnicfNTPPeerDispersion_Type.__name__=_C
_HpnicfNTPPeerDispersion_Object=MibTableColumn
hpnicfNTPPeerDispersion=_HpnicfNTPPeerDispersion_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,27),_HpnicfNTPPeerDispersion_Type())
hpnicfNTPPeerDispersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerDispersion.setStatus(_A)
class _HpnicfNTPPeerKeyId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HpnicfNTPPeerKeyId_Type.__name__=_E
_HpnicfNTPPeerKeyId_Object=MibTableColumn
hpnicfNTPPeerKeyId=_HpnicfNTPPeerKeyId_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,28),_HpnicfNTPPeerKeyId_Type())
hpnicfNTPPeerKeyId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerKeyId.setStatus(_A)
class _HpnicfNTPPeerFiltDelay_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HpnicfNTPPeerFiltDelay_Type.__name__=_C
_HpnicfNTPPeerFiltDelay_Object=MibTableColumn
hpnicfNTPPeerFiltDelay=_HpnicfNTPPeerFiltDelay_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,29),_HpnicfNTPPeerFiltDelay_Type())
hpnicfNTPPeerFiltDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerFiltDelay.setStatus(_A)
class _HpnicfNTPPeerFiltOffset_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HpnicfNTPPeerFiltOffset_Type.__name__=_C
_HpnicfNTPPeerFiltOffset_Object=MibTableColumn
hpnicfNTPPeerFiltOffset=_HpnicfNTPPeerFiltOffset_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,30),_HpnicfNTPPeerFiltOffset_Type())
hpnicfNTPPeerFiltOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerFiltOffset.setStatus(_A)
class _HpnicfNTPPeerFiltError_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HpnicfNTPPeerFiltError_Type.__name__=_C
_HpnicfNTPPeerFiltError_Object=MibTableColumn
hpnicfNTPPeerFiltError=_HpnicfNTPPeerFiltError_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,31),_HpnicfNTPPeerFiltError_Type())
hpnicfNTPPeerFiltError.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerFiltError.setStatus(_A)
class _HpnicfNTPPeerPMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_N,0),(_O,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),(_V,8),(_W,9)))
_HpnicfNTPPeerPMode_Type.__name__=_D
_HpnicfNTPPeerPMode_Object=MibTableColumn
hpnicfNTPPeerPMode=_HpnicfNTPPeerPMode_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,32),_HpnicfNTPPeerPMode_Type())
hpnicfNTPPeerPMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerPMode.setStatus(_A)
_HpnicfNTPPeerReceived_Type=Counter32
_HpnicfNTPPeerReceived_Object=MibTableColumn
hpnicfNTPPeerReceived=_HpnicfNTPPeerReceived_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,33),_HpnicfNTPPeerReceived_Type())
hpnicfNTPPeerReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerReceived.setStatus(_A)
_HpnicfNTPPeerSent_Type=Counter32
_HpnicfNTPPeerSent_Object=MibTableColumn
hpnicfNTPPeerSent=_HpnicfNTPPeerSent_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,34),_HpnicfNTPPeerSent_Type())
hpnicfNTPPeerSent.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerSent.setStatus(_A)
class _HpnicfNTPPeerFlash_Type(Bits):namedValues=NamedValues(*(('recvRepeatMsg',0),('recvremanMsg',1),('unSynMsg',2),('dispBeyond',3),('unauthenticate',4),('unSynClock',5),('straBeyond',6),('rootDispBeyond',7),('noAuthen',8),('refuOperate',9)))
_HpnicfNTPPeerFlash_Type.__name__='Bits'
_HpnicfNTPPeerFlash_Object=MibTableColumn
hpnicfNTPPeerFlash=_HpnicfNTPPeerFlash_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,35),_HpnicfNTPPeerFlash_Type())
hpnicfNTPPeerFlash.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNTPPeerFlash.setStatus(_A)
_HpnicfNTPPeerRowStatus_Type=RowStatus
_HpnicfNTPPeerRowStatus_Object=MibTableColumn
hpnicfNTPPeerRowStatus=_HpnicfNTPPeerRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,22,2,1,1,1,36),_HpnicfNTPPeerRowStatus_Type())
hpnicfNTPPeerRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:hpnicfNTPPeerRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'hpnicfNTP':hpnicfNTP,'hpnicfNTPSystemMIB':hpnicfNTPSystemMIB,'hpnicfNTPSystemMIBObjects':hpnicfNTPSystemMIBObjects,'hpnicfNTPSysLeap':hpnicfNTPSysLeap,'hpnicfNTPSysStratum':hpnicfNTPSysStratum,'hpnicfNTPSysPrecision':hpnicfNTPSysPrecision,'hpnicfNTPSysRootdelay':hpnicfNTPSysRootdelay,'hpnicfNTPSysRootdispersion':hpnicfNTPSysRootdispersion,'hpnicfNTPSysRefid':hpnicfNTPSysRefid,'hpnicfNTPSysReftime':hpnicfNTPSysReftime,'hpnicfNTPSysPoll':hpnicfNTPSysPoll,'hpnicfNTPSysPeer':hpnicfNTPSysPeer,'hpnicfNTPSysState':hpnicfNTPSysState,'hpnicfNTPSysOffset':hpnicfNTPSysOffset,'hpnicfNTPSysDrift':hpnicfNTPSysDrift,'hpnicfNTPSysCompliance':hpnicfNTPSysCompliance,'hpnicfNTPSysClock':hpnicfNTPSysClock,'hpnicfNTPSysStabil':hpnicfNTPSysStabil,'hpnicfNTPSysAuthenticate':hpnicfNTPSysAuthenticate,'hpnicfNTPSysPollSec':hpnicfNTPSysPollSec,'hpnicfNTPSysClockSec':hpnicfNTPSysClockSec,'hpnicfNTPServerIP':hpnicfNTPServerIP,'hpnicfNTPSysSrcPeer':hpnicfNTPSysSrcPeer,'hpnicfNTPPeerMIB':hpnicfNTPPeerMIB,'hpnicfNTPPeerMIBObjects':hpnicfNTPPeerMIBObjects,'hpnicfNTPPeerTable':hpnicfNTPPeerTable,'hpnicfNTPPeerEntry':hpnicfNTPPeerEntry,'hpnicfNTPPeerConfig':hpnicfNTPPeerConfig,'hpnicfNTPPeerAuthenable':hpnicfNTPPeerAuthenable,'hpnicfNTPPeerAuthentic':hpnicfNTPPeerAuthentic,_K:hpnicfNTPPeerRemAdr,'hpnicfNTPPeerRemPort':hpnicfNTPPeerRemPort,'hpnicfNTPPeerLocAdr':hpnicfNTPPeerLocAdr,'hpnicfNTPPeerLocPort':hpnicfNTPPeerLocPort,'hpnicfNTPPeerLeap':hpnicfNTPPeerLeap,_L:hpnicfNTPPeerHMode,'hpnicfNTPPeerStratum':hpnicfNTPPeerStratum,'hpnicfNTPPeerPPoll':hpnicfNTPPeerPPoll,'hpnicfNTPPeerHPoll':hpnicfNTPPeerHPoll,'hpnicfNTPPeerPrecision':hpnicfNTPPeerPrecision,'hpnicfNTPPeerRootDelay':hpnicfNTPPeerRootDelay,'hpnicfNTPPeerRootDispersion':hpnicfNTPPeerRootDispersion,'hpnicfNTPPeerRefId':hpnicfNTPPeerRefId,'hpnicfNTPPeerRefTime':hpnicfNTPPeerRefTime,'hpnicfNTPPeerOrg':hpnicfNTPPeerOrg,'hpnicfNTPPeerRec':hpnicfNTPPeerRec,'hpnicfNTPPeerXmt':hpnicfNTPPeerXmt,'hpnicfNTPPeerReach':hpnicfNTPPeerReach,'hpnicfNTPPeerValid':hpnicfNTPPeerValid,'hpnicfNTPPeerTimer':hpnicfNTPPeerTimer,'hpnicfNTPPeerDelay':hpnicfNTPPeerDelay,'hpnicfNTPPeerOffset':hpnicfNTPPeerOffset,'hpnicfNTPPeerJitter':hpnicfNTPPeerJitter,'hpnicfNTPPeerDispersion':hpnicfNTPPeerDispersion,'hpnicfNTPPeerKeyId':hpnicfNTPPeerKeyId,'hpnicfNTPPeerFiltDelay':hpnicfNTPPeerFiltDelay,'hpnicfNTPPeerFiltOffset':hpnicfNTPPeerFiltOffset,'hpnicfNTPPeerFiltError':hpnicfNTPPeerFiltError,'hpnicfNTPPeerPMode':hpnicfNTPPeerPMode,'hpnicfNTPPeerReceived':hpnicfNTPPeerReceived,'hpnicfNTPPeerSent':hpnicfNTPPeerSent,'hpnicfNTPPeerFlash':hpnicfNTPPeerFlash,'hpnicfNTPPeerRowStatus':hpnicfNTPPeerRowStatus})