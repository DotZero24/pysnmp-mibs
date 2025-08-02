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
_L='hwNTPPeerHMode'
_K='hwNTPPeerRemAdr'
_J='subtractSecond'
_I='addSecond'
_H='noWarning'
_G='Unsigned32'
_F='A3COM-HUAWEI-NTP-MIB'
_E='read-write'
_D='Integer32'
_C='OctetString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
huaweiDatacomm,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','huaweiDatacomm')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
hwNTP=ModuleIdentity((1,3,6,1,4,1,43,45,1,5,25,22))
if mibBuilder.loadTexts:hwNTP.setRevisions(('2003-03-15 00:00',))
_HwNTPSystemMIB_ObjectIdentity=ObjectIdentity
hwNTPSystemMIB=_HwNTPSystemMIB_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,22,1))
_HwNTPSystemMIBObjects_ObjectIdentity=ObjectIdentity
hwNTPSystemMIBObjects=_HwNTPSystemMIBObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,22,1,1))
class _HwNTPSysLeap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_H,0),(_I,1),(_J,2),('alarm',3)))
_HwNTPSysLeap_Type.__name__=_D
_HwNTPSysLeap_Object=MibScalar
hwNTPSysLeap=_HwNTPSysLeap_Object((1,3,6,1,4,1,43,45,1,5,25,22,1,1,1),_HwNTPSysLeap_Type())
hwNTPSysLeap.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPSysLeap.setStatus(_A)
class _HwNTPSysStratum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HwNTPSysStratum_Type.__name__=_D
_HwNTPSysStratum_Object=MibScalar
hwNTPSysStratum=_HwNTPSysStratum_Object((1,3,6,1,4,1,43,45,1,5,25,22,1,1,2),_HwNTPSysStratum_Type())
hwNTPSysStratum.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPSysStratum.setStatus(_A)
class _HwNTPSysPrecision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-20,20))
_HwNTPSysPrecision_Type.__name__=_D
_HwNTPSysPrecision_Object=MibScalar
hwNTPSysPrecision=_HwNTPSysPrecision_Object((1,3,6,1,4,1,43,45,1,5,25,22,1,1,3),_HwNTPSysPrecision_Type())
hwNTPSysPrecision.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPSysPrecision.setStatus(_A)
class _HwNTPSysRootdelay_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HwNTPSysRootdelay_Type.__name__=_C
_HwNTPSysRootdelay_Object=MibScalar
hwNTPSysRootdelay=_HwNTPSysRootdelay_Object((1,3,6,1,4,1,43,45,1,5,25,22,1,1,4),_HwNTPSysRootdelay_Type())
hwNTPSysRootdelay.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPSysRootdelay.setStatus(_A)
class _HwNTPSysRootdispersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HwNTPSysRootdispersion_Type.__name__=_C
_HwNTPSysRootdispersion_Object=MibScalar
hwNTPSysRootdispersion=_HwNTPSysRootdispersion_Object((1,3,6,1,4,1,43,45,1,5,25,22,1,1,5),_HwNTPSysRootdispersion_Type())
hwNTPSysRootdispersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPSysRootdispersion.setStatus(_A)
class _HwNTPSysRefid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HwNTPSysRefid_Type.__name__=_C
_HwNTPSysRefid_Object=MibScalar
hwNTPSysRefid=_HwNTPSysRefid_Object((1,3,6,1,4,1,43,45,1,5,25,22,1,1,6),_HwNTPSysRefid_Type())
hwNTPSysRefid.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPSysRefid.setStatus(_A)
class _HwNTPSysReftime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HwNTPSysReftime_Type.__name__=_C
_HwNTPSysReftime_Object=MibScalar
hwNTPSysReftime=_HwNTPSysReftime_Object((1,3,6,1,4,1,43,45,1,5,25,22,1,1,7),_HwNTPSysReftime_Type())
hwNTPSysReftime.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPSysReftime.setStatus(_A)
class _HwNTPSysPoll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-20,20))
_HwNTPSysPoll_Type.__name__=_D
_HwNTPSysPoll_Object=MibScalar
hwNTPSysPoll=_HwNTPSysPoll_Object((1,3,6,1,4,1,43,45,1,5,25,22,1,1,8),_HwNTPSysPoll_Type())
hwNTPSysPoll.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPSysPoll.setStatus(_A)
class _HwNTPSysPeer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HwNTPSysPeer_Type.__name__=_D
_HwNTPSysPeer_Object=MibScalar
hwNTPSysPeer=_HwNTPSysPeer_Object((1,3,6,1,4,1,43,45,1,5,25,22,1,1,9),_HwNTPSysPeer_Type())
hwNTPSysPeer.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPSysPeer.setStatus(_A)
class _HwNTPSysState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('noUpdateClock',0),('getfreqInfo',1),('clockBySet',2),('clockBySetAndNoFreq',3),('clockBySyns',4),('findError',5)))
_HwNTPSysState_Type.__name__=_D
_HwNTPSysState_Object=MibScalar
hwNTPSysState=_HwNTPSysState_Object((1,3,6,1,4,1,43,45,1,5,25,22,1,1,10),_HwNTPSysState_Type())
hwNTPSysState.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPSysState.setStatus(_A)
class _HwNTPSysOffset_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HwNTPSysOffset_Type.__name__=_C
_HwNTPSysOffset_Object=MibScalar
hwNTPSysOffset=_HwNTPSysOffset_Object((1,3,6,1,4,1,43,45,1,5,25,22,1,1,11),_HwNTPSysOffset_Type())
hwNTPSysOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPSysOffset.setStatus(_A)
class _HwNTPSysDrift_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HwNTPSysDrift_Type.__name__=_C
_HwNTPSysDrift_Object=MibScalar
hwNTPSysDrift=_HwNTPSysDrift_Object((1,3,6,1,4,1,43,45,1,5,25,22,1,1,12),_HwNTPSysDrift_Type())
hwNTPSysDrift.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPSysDrift.setStatus(_A)
class _HwNTPSysCompliance_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HwNTPSysCompliance_Type.__name__=_C
_HwNTPSysCompliance_Object=MibScalar
hwNTPSysCompliance=_HwNTPSysCompliance_Object((1,3,6,1,4,1,43,45,1,5,25,22,1,1,13),_HwNTPSysCompliance_Type())
hwNTPSysCompliance.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPSysCompliance.setStatus(_A)
class _HwNTPSysClock_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HwNTPSysClock_Type.__name__=_C
_HwNTPSysClock_Object=MibScalar
hwNTPSysClock=_HwNTPSysClock_Object((1,3,6,1,4,1,43,45,1,5,25,22,1,1,14),_HwNTPSysClock_Type())
hwNTPSysClock.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPSysClock.setStatus(_A)
class _HwNTPSysStabil_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HwNTPSysStabil_Type.__name__=_C
_HwNTPSysStabil_Object=MibScalar
hwNTPSysStabil=_HwNTPSysStabil_Object((1,3,6,1,4,1,43,45,1,5,25,22,1,1,15),_HwNTPSysStabil_Type())
hwNTPSysStabil.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPSysStabil.setStatus(_A)
class _HwNTPSysAuthenticate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noAuthenticate',0),('authenticate',1)))
_HwNTPSysAuthenticate_Type.__name__=_D
_HwNTPSysAuthenticate_Object=MibScalar
hwNTPSysAuthenticate=_HwNTPSysAuthenticate_Object((1,3,6,1,4,1,43,45,1,5,25,22,1,1,16),_HwNTPSysAuthenticate_Type())
hwNTPSysAuthenticate.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNTPSysAuthenticate.setStatus(_A)
class _HwNTPSysPollSec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,1048576))
_HwNTPSysPollSec_Type.__name__=_D
_HwNTPSysPollSec_Object=MibScalar
hwNTPSysPollSec=_HwNTPSysPollSec_Object((1,3,6,1,4,1,43,45,1,5,25,22,1,1,17),_HwNTPSysPollSec_Type())
hwNTPSysPollSec.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNTPSysPollSec.setStatus(_A)
_HwNTPSysClockSec_Type=Integer32
_HwNTPSysClockSec_Object=MibScalar
hwNTPSysClockSec=_HwNTPSysClockSec_Object((1,3,6,1,4,1,43,45,1,5,25,22,1,1,18),_HwNTPSysClockSec_Type())
hwNTPSysClockSec.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPSysClockSec.setStatus(_A)
_HwNTPServerIP_Type=IpAddress
_HwNTPServerIP_Object=MibScalar
hwNTPServerIP=_HwNTPServerIP_Object((1,3,6,1,4,1,43,45,1,5,25,22,1,1,19),_HwNTPServerIP_Type())
hwNTPServerIP.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNTPServerIP.setStatus(_A)
_HwNTPPeerMIB_ObjectIdentity=ObjectIdentity
hwNTPPeerMIB=_HwNTPPeerMIB_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,22,2))
_HwNTPPeerMIBObjects_ObjectIdentity=ObjectIdentity
hwNTPPeerMIBObjects=_HwNTPPeerMIBObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,22,2,1))
_HwNTPPeerTable_Object=MibTable
hwNTPPeerTable=_HwNTPPeerTable_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1))
if mibBuilder.loadTexts:hwNTPPeerTable.setStatus(_A)
_HwNTPPeerEntry_Object=MibTableRow
hwNTPPeerEntry=_HwNTPPeerEntry_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1))
hwNTPPeerEntry.setIndexNames((0,_F,_K),(0,_F,_L))
if mibBuilder.loadTexts:hwNTPPeerEntry.setStatus(_A)
_HwNTPPeerConfig_Type=TruthValue
_HwNTPPeerConfig_Object=MibTableColumn
hwNTPPeerConfig=_HwNTPPeerConfig_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,1),_HwNTPPeerConfig_Type())
hwNTPPeerConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerConfig.setStatus(_A)
_HwNTPPeerAuthenable_Type=TruthValue
_HwNTPPeerAuthenable_Object=MibTableColumn
hwNTPPeerAuthenable=_HwNTPPeerAuthenable_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,2),_HwNTPPeerAuthenable_Type())
hwNTPPeerAuthenable.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerAuthenable.setStatus(_A)
_HwNTPPeerAuthentic_Type=TruthValue
_HwNTPPeerAuthentic_Object=MibTableColumn
hwNTPPeerAuthentic=_HwNTPPeerAuthentic_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,3),_HwNTPPeerAuthentic_Type())
hwNTPPeerAuthentic.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerAuthentic.setStatus(_A)
_HwNTPPeerRemAdr_Type=IpAddress
_HwNTPPeerRemAdr_Object=MibTableColumn
hwNTPPeerRemAdr=_HwNTPPeerRemAdr_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,4),_HwNTPPeerRemAdr_Type())
hwNTPPeerRemAdr.setMaxAccess(_M)
if mibBuilder.loadTexts:hwNTPPeerRemAdr.setStatus(_A)
class _HwNTPPeerRemPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HwNTPPeerRemPort_Type.__name__=_D
_HwNTPPeerRemPort_Object=MibTableColumn
hwNTPPeerRemPort=_HwNTPPeerRemPort_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,5),_HwNTPPeerRemPort_Type())
hwNTPPeerRemPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerRemPort.setStatus(_A)
_HwNTPPeerLocAdr_Type=IpAddress
_HwNTPPeerLocAdr_Object=MibTableColumn
hwNTPPeerLocAdr=_HwNTPPeerLocAdr_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,6),_HwNTPPeerLocAdr_Type())
hwNTPPeerLocAdr.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerLocAdr.setStatus(_A)
class _HwNTPPeerLocPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HwNTPPeerLocPort_Type.__name__=_D
_HwNTPPeerLocPort_Object=MibTableColumn
hwNTPPeerLocPort=_HwNTPPeerLocPort_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,7),_HwNTPPeerLocPort_Type())
hwNTPPeerLocPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerLocPort.setStatus(_A)
class _HwNTPPeerLeap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_H,0),(_I,1),(_J,2),('alarm',3)))
_HwNTPPeerLeap_Type.__name__=_D
_HwNTPPeerLeap_Object=MibTableColumn
hwNTPPeerLeap=_HwNTPPeerLeap_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,8),_HwNTPPeerLeap_Type())
hwNTPPeerLeap.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerLeap.setStatus(_A)
class _HwNTPPeerHMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_N,0),(_O,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),(_V,8),(_W,9)))
_HwNTPPeerHMode_Type.__name__=_D
_HwNTPPeerHMode_Object=MibTableColumn
hwNTPPeerHMode=_HwNTPPeerHMode_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,9),_HwNTPPeerHMode_Type())
hwNTPPeerHMode.setMaxAccess(_M)
if mibBuilder.loadTexts:hwNTPPeerHMode.setStatus(_A)
class _HwNTPPeerStratum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HwNTPPeerStratum_Type.__name__=_D
_HwNTPPeerStratum_Object=MibTableColumn
hwNTPPeerStratum=_HwNTPPeerStratum_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,10),_HwNTPPeerStratum_Type())
hwNTPPeerStratum.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerStratum.setStatus(_A)
class _HwNTPPeerPPoll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-20,20))
_HwNTPPeerPPoll_Type.__name__=_D
_HwNTPPeerPPoll_Object=MibTableColumn
hwNTPPeerPPoll=_HwNTPPeerPPoll_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,11),_HwNTPPeerPPoll_Type())
hwNTPPeerPPoll.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerPPoll.setStatus(_A)
class _HwNTPPeerHPoll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-20,20))
_HwNTPPeerHPoll_Type.__name__=_D
_HwNTPPeerHPoll_Object=MibTableColumn
hwNTPPeerHPoll=_HwNTPPeerHPoll_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,12),_HwNTPPeerHPoll_Type())
hwNTPPeerHPoll.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerHPoll.setStatus(_A)
class _HwNTPPeerPrecision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-20,20))
_HwNTPPeerPrecision_Type.__name__=_D
_HwNTPPeerPrecision_Object=MibTableColumn
hwNTPPeerPrecision=_HwNTPPeerPrecision_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,13),_HwNTPPeerPrecision_Type())
hwNTPPeerPrecision.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerPrecision.setStatus(_A)
class _HwNTPPeerRootDelay_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HwNTPPeerRootDelay_Type.__name__=_C
_HwNTPPeerRootDelay_Object=MibTableColumn
hwNTPPeerRootDelay=_HwNTPPeerRootDelay_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,14),_HwNTPPeerRootDelay_Type())
hwNTPPeerRootDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerRootDelay.setStatus(_A)
class _HwNTPPeerRootDispersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HwNTPPeerRootDispersion_Type.__name__=_C
_HwNTPPeerRootDispersion_Object=MibTableColumn
hwNTPPeerRootDispersion=_HwNTPPeerRootDispersion_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,15),_HwNTPPeerRootDispersion_Type())
hwNTPPeerRootDispersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerRootDispersion.setStatus(_A)
class _HwNTPPeerRefId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HwNTPPeerRefId_Type.__name__=_C
_HwNTPPeerRefId_Object=MibTableColumn
hwNTPPeerRefId=_HwNTPPeerRefId_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,16),_HwNTPPeerRefId_Type())
hwNTPPeerRefId.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerRefId.setStatus(_A)
class _HwNTPPeerRefTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HwNTPPeerRefTime_Type.__name__=_C
_HwNTPPeerRefTime_Object=MibTableColumn
hwNTPPeerRefTime=_HwNTPPeerRefTime_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,17),_HwNTPPeerRefTime_Type())
hwNTPPeerRefTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerRefTime.setStatus(_A)
class _HwNTPPeerOrg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HwNTPPeerOrg_Type.__name__=_C
_HwNTPPeerOrg_Object=MibTableColumn
hwNTPPeerOrg=_HwNTPPeerOrg_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,18),_HwNTPPeerOrg_Type())
hwNTPPeerOrg.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerOrg.setStatus(_A)
class _HwNTPPeerRec_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HwNTPPeerRec_Type.__name__=_C
_HwNTPPeerRec_Object=MibTableColumn
hwNTPPeerRec=_HwNTPPeerRec_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,19),_HwNTPPeerRec_Type())
hwNTPPeerRec.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerRec.setStatus(_A)
class _HwNTPPeerXmt_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HwNTPPeerXmt_Type.__name__=_C
_HwNTPPeerXmt_Object=MibTableColumn
hwNTPPeerXmt=_HwNTPPeerXmt_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,20),_HwNTPPeerXmt_Type())
hwNTPPeerXmt.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerXmt.setStatus(_A)
class _HwNTPPeerReach_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HwNTPPeerReach_Type.__name__=_D
_HwNTPPeerReach_Object=MibTableColumn
hwNTPPeerReach=_HwNTPPeerReach_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,21),_HwNTPPeerReach_Type())
hwNTPPeerReach.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerReach.setStatus(_A)
class _HwNTPPeerValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HwNTPPeerValid_Type.__name__=_D
_HwNTPPeerValid_Object=MibTableColumn
hwNTPPeerValid=_HwNTPPeerValid_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,22),_HwNTPPeerValid_Type())
hwNTPPeerValid.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerValid.setStatus(_A)
class _HwNTPPeerTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HwNTPPeerTimer_Type.__name__=_D
_HwNTPPeerTimer_Object=MibTableColumn
hwNTPPeerTimer=_HwNTPPeerTimer_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,23),_HwNTPPeerTimer_Type())
hwNTPPeerTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerTimer.setStatus(_A)
class _HwNTPPeerDelay_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HwNTPPeerDelay_Type.__name__=_C
_HwNTPPeerDelay_Object=MibTableColumn
hwNTPPeerDelay=_HwNTPPeerDelay_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,24),_HwNTPPeerDelay_Type())
hwNTPPeerDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerDelay.setStatus(_A)
class _HwNTPPeerOffset_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HwNTPPeerOffset_Type.__name__=_C
_HwNTPPeerOffset_Object=MibTableColumn
hwNTPPeerOffset=_HwNTPPeerOffset_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,25),_HwNTPPeerOffset_Type())
hwNTPPeerOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerOffset.setStatus(_A)
class _HwNTPPeerJitter_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HwNTPPeerJitter_Type.__name__=_C
_HwNTPPeerJitter_Object=MibTableColumn
hwNTPPeerJitter=_HwNTPPeerJitter_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,26),_HwNTPPeerJitter_Type())
hwNTPPeerJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerJitter.setStatus(_A)
class _HwNTPPeerDispersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HwNTPPeerDispersion_Type.__name__=_C
_HwNTPPeerDispersion_Object=MibTableColumn
hwNTPPeerDispersion=_HwNTPPeerDispersion_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,27),_HwNTPPeerDispersion_Type())
hwNTPPeerDispersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerDispersion.setStatus(_A)
class _HwNTPPeerKeyId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HwNTPPeerKeyId_Type.__name__=_G
_HwNTPPeerKeyId_Object=MibTableColumn
hwNTPPeerKeyId=_HwNTPPeerKeyId_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,28),_HwNTPPeerKeyId_Type())
hwNTPPeerKeyId.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerKeyId.setStatus(_A)
class _HwNTPPeerFiltDelay_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HwNTPPeerFiltDelay_Type.__name__=_C
_HwNTPPeerFiltDelay_Object=MibTableColumn
hwNTPPeerFiltDelay=_HwNTPPeerFiltDelay_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,29),_HwNTPPeerFiltDelay_Type())
hwNTPPeerFiltDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerFiltDelay.setStatus(_A)
class _HwNTPPeerFiltOffset_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HwNTPPeerFiltOffset_Type.__name__=_C
_HwNTPPeerFiltOffset_Object=MibTableColumn
hwNTPPeerFiltOffset=_HwNTPPeerFiltOffset_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,30),_HwNTPPeerFiltOffset_Type())
hwNTPPeerFiltOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerFiltOffset.setStatus(_A)
class _HwNTPPeerFiltError_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HwNTPPeerFiltError_Type.__name__=_C
_HwNTPPeerFiltError_Object=MibTableColumn
hwNTPPeerFiltError=_HwNTPPeerFiltError_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,31),_HwNTPPeerFiltError_Type())
hwNTPPeerFiltError.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerFiltError.setStatus(_A)
class _HwNTPPeerPMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_N,0),(_O,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),(_V,8),(_W,9)))
_HwNTPPeerPMode_Type.__name__=_D
_HwNTPPeerPMode_Object=MibTableColumn
hwNTPPeerPMode=_HwNTPPeerPMode_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,32),_HwNTPPeerPMode_Type())
hwNTPPeerPMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerPMode.setStatus(_A)
_HwNTPPeerReceived_Type=Counter32
_HwNTPPeerReceived_Object=MibTableColumn
hwNTPPeerReceived=_HwNTPPeerReceived_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,33),_HwNTPPeerReceived_Type())
hwNTPPeerReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerReceived.setStatus(_A)
_HwNTPPeerSent_Type=Counter32
_HwNTPPeerSent_Object=MibTableColumn
hwNTPPeerSent=_HwNTPPeerSent_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,34),_HwNTPPeerSent_Type())
hwNTPPeerSent.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerSent.setStatus(_A)
class _HwNTPPeerFlash_Type(Bits):namedValues=NamedValues(*(('recvRepeatMsg',0),('recvremanMsg',1),('unSynMsg',2),('dispBeyond',3),('unauthenticate',4),('unSynClock',5),('straBeyond',6),('rootDispBeyond',7),('noAuthen',8),('refuOperate',9)))
_HwNTPPeerFlash_Type.__name__='Bits'
_HwNTPPeerFlash_Object=MibTableColumn
hwNTPPeerFlash=_HwNTPPeerFlash_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,35),_HwNTPPeerFlash_Type())
hwNTPPeerFlash.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNTPPeerFlash.setStatus(_A)
_HwNTPPeerRowStatus_Type=RowStatus
_HwNTPPeerRowStatus_Object=MibTableColumn
hwNTPPeerRowStatus=_HwNTPPeerRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,22,2,1,1,1,36),_HwNTPPeerRowStatus_Type())
hwNTPPeerRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:hwNTPPeerRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'hwNTP':hwNTP,'hwNTPSystemMIB':hwNTPSystemMIB,'hwNTPSystemMIBObjects':hwNTPSystemMIBObjects,'hwNTPSysLeap':hwNTPSysLeap,'hwNTPSysStratum':hwNTPSysStratum,'hwNTPSysPrecision':hwNTPSysPrecision,'hwNTPSysRootdelay':hwNTPSysRootdelay,'hwNTPSysRootdispersion':hwNTPSysRootdispersion,'hwNTPSysRefid':hwNTPSysRefid,'hwNTPSysReftime':hwNTPSysReftime,'hwNTPSysPoll':hwNTPSysPoll,'hwNTPSysPeer':hwNTPSysPeer,'hwNTPSysState':hwNTPSysState,'hwNTPSysOffset':hwNTPSysOffset,'hwNTPSysDrift':hwNTPSysDrift,'hwNTPSysCompliance':hwNTPSysCompliance,'hwNTPSysClock':hwNTPSysClock,'hwNTPSysStabil':hwNTPSysStabil,'hwNTPSysAuthenticate':hwNTPSysAuthenticate,'hwNTPSysPollSec':hwNTPSysPollSec,'hwNTPSysClockSec':hwNTPSysClockSec,'hwNTPServerIP':hwNTPServerIP,'hwNTPPeerMIB':hwNTPPeerMIB,'hwNTPPeerMIBObjects':hwNTPPeerMIBObjects,'hwNTPPeerTable':hwNTPPeerTable,'hwNTPPeerEntry':hwNTPPeerEntry,'hwNTPPeerConfig':hwNTPPeerConfig,'hwNTPPeerAuthenable':hwNTPPeerAuthenable,'hwNTPPeerAuthentic':hwNTPPeerAuthentic,_K:hwNTPPeerRemAdr,'hwNTPPeerRemPort':hwNTPPeerRemPort,'hwNTPPeerLocAdr':hwNTPPeerLocAdr,'hwNTPPeerLocPort':hwNTPPeerLocPort,'hwNTPPeerLeap':hwNTPPeerLeap,_L:hwNTPPeerHMode,'hwNTPPeerStratum':hwNTPPeerStratum,'hwNTPPeerPPoll':hwNTPPeerPPoll,'hwNTPPeerHPoll':hwNTPPeerHPoll,'hwNTPPeerPrecision':hwNTPPeerPrecision,'hwNTPPeerRootDelay':hwNTPPeerRootDelay,'hwNTPPeerRootDispersion':hwNTPPeerRootDispersion,'hwNTPPeerRefId':hwNTPPeerRefId,'hwNTPPeerRefTime':hwNTPPeerRefTime,'hwNTPPeerOrg':hwNTPPeerOrg,'hwNTPPeerRec':hwNTPPeerRec,'hwNTPPeerXmt':hwNTPPeerXmt,'hwNTPPeerReach':hwNTPPeerReach,'hwNTPPeerValid':hwNTPPeerValid,'hwNTPPeerTimer':hwNTPPeerTimer,'hwNTPPeerDelay':hwNTPPeerDelay,'hwNTPPeerOffset':hwNTPPeerOffset,'hwNTPPeerJitter':hwNTPPeerJitter,'hwNTPPeerDispersion':hwNTPPeerDispersion,'hwNTPPeerKeyId':hwNTPPeerKeyId,'hwNTPPeerFiltDelay':hwNTPPeerFiltDelay,'hwNTPPeerFiltOffset':hwNTPPeerFiltOffset,'hwNTPPeerFiltError':hwNTPPeerFiltError,'hwNTPPeerPMode':hwNTPPeerPMode,'hwNTPPeerReceived':hwNTPPeerReceived,'hwNTPPeerSent':hwNTPPeerSent,'hwNTPPeerFlash':hwNTPPeerFlash,'hwNTPPeerRowStatus':hwNTPPeerRowStatus})