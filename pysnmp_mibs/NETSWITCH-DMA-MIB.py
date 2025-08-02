_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_Nm_ObjectIdentity=ObjectIdentity
nm=_Nm_ObjectIdentity((1,3,6,1,4,1,11,2))
_Icf_ObjectIdentity=ObjectIdentity
icf=_Icf_ObjectIdentity((1,3,6,1,4,1,11,2,14))
_HpicfObjects_ObjectIdentity=ObjectIdentity
hpicfObjects=_HpicfObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11))
_HpicfSwitch_ObjectIdentity=ObjectIdentity
hpicfSwitch=_HpicfSwitch_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5))
_HpSwitch_ObjectIdentity=ObjectIdentity
hpSwitch=_HpSwitch_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1))
_HpOpSystem_ObjectIdentity=ObjectIdentity
hpOpSystem=_HpOpSystem_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,1))
_HpHwSystem_ObjectIdentity=ObjectIdentity
hpHwSystem=_HpHwSystem_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,2))
_HpDMAStats_ObjectIdentity=ObjectIdentity
hpDMAStats=_HpDMAStats_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,2,2))
class _HpDMAReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_HpDMAReset_Type.__name__=_C
_HpDMAReset_Object=MibScalar
hpDMAReset=_HpDMAReset_Object((1,3,6,1,4,1,11,2,14,11,5,1,2,2,1),_HpDMAReset_Type())
hpDMAReset.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpDMAReset.setStatus(_A)
_HpDMAFrameRcvcnt_Type=Counter32
_HpDMAFrameRcvcnt_Object=MibScalar
hpDMAFrameRcvcnt=_HpDMAFrameRcvcnt_Object((1,3,6,1,4,1,11,2,14,11,5,1,2,2,2),_HpDMAFrameRcvcnt_Type())
hpDMAFrameRcvcnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpDMAFrameRcvcnt.setStatus(_A)
_HpDMAOctetsRcvcnt_Type=Counter32
_HpDMAOctetsRcvcnt_Object=MibScalar
hpDMAOctetsRcvcnt=_HpDMAOctetsRcvcnt_Object((1,3,6,1,4,1,11,2,14,11,5,1,2,2,3),_HpDMAOctetsRcvcnt_Type())
hpDMAOctetsRcvcnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpDMAOctetsRcvcnt.setStatus(_A)
_HpDMAPrevRcvFrames_Type=Counter32
_HpDMAPrevRcvFrames_Object=MibScalar
hpDMAPrevRcvFrames=_HpDMAPrevRcvFrames_Object((1,3,6,1,4,1,11,2,14,11,5,1,2,2,4),_HpDMAPrevRcvFrames_Type())
hpDMAPrevRcvFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:hpDMAPrevRcvFrames.setStatus(_A)
_HpDMAFrameRcvPerSec_Type=Counter32
_HpDMAFrameRcvPerSec_Object=MibScalar
hpDMAFrameRcvPerSec=_HpDMAFrameRcvPerSec_Object((1,3,6,1,4,1,11,2,14,11,5,1,2,2,5),_HpDMAFrameRcvPerSec_Type())
hpDMAFrameRcvPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:hpDMAFrameRcvPerSec.setStatus(_A)
_HpDMAPeakRcvFrames_Type=Counter32
_HpDMAPeakRcvFrames_Object=MibScalar
hpDMAPeakRcvFrames=_HpDMAPeakRcvFrames_Object((1,3,6,1,4,1,11,2,14,11,5,1,2,2,6),_HpDMAPeakRcvFrames_Type())
hpDMAPeakRcvFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:hpDMAPeakRcvFrames.setStatus(_A)
_HpDMAPrevRcvOctets_Type=Counter32
_HpDMAPrevRcvOctets_Object=MibScalar
hpDMAPrevRcvOctets=_HpDMAPrevRcvOctets_Object((1,3,6,1,4,1,11,2,14,11,5,1,2,2,7),_HpDMAPrevRcvOctets_Type())
hpDMAPrevRcvOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:hpDMAPrevRcvOctets.setStatus(_A)
_HpDMAOctetsRcvPerSec_Type=Counter32
_HpDMAOctetsRcvPerSec_Object=MibScalar
hpDMAOctetsRcvPerSec=_HpDMAOctetsRcvPerSec_Object((1,3,6,1,4,1,11,2,14,11,5,1,2,2,8),_HpDMAOctetsRcvPerSec_Type())
hpDMAOctetsRcvPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:hpDMAOctetsRcvPerSec.setStatus(_A)
_HpDMAPeakRcvOctets_Type=Counter32
_HpDMAPeakRcvOctets_Object=MibScalar
hpDMAPeakRcvOctets=_HpDMAPeakRcvOctets_Object((1,3,6,1,4,1,11,2,14,11,5,1,2,2,9),_HpDMAPeakRcvOctets_Type())
hpDMAPeakRcvOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:hpDMAPeakRcvOctets.setStatus(_A)
_HpDMAFrameXmtcnt_Type=Counter32
_HpDMAFrameXmtcnt_Object=MibScalar
hpDMAFrameXmtcnt=_HpDMAFrameXmtcnt_Object((1,3,6,1,4,1,11,2,14,11,5,1,2,2,10),_HpDMAFrameXmtcnt_Type())
hpDMAFrameXmtcnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpDMAFrameXmtcnt.setStatus(_A)
_HpDMAOctetsXmtcnt_Type=Counter32
_HpDMAOctetsXmtcnt_Object=MibScalar
hpDMAOctetsXmtcnt=_HpDMAOctetsXmtcnt_Object((1,3,6,1,4,1,11,2,14,11,5,1,2,2,11),_HpDMAOctetsXmtcnt_Type())
hpDMAOctetsXmtcnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpDMAOctetsXmtcnt.setStatus(_A)
_HpDMAPrevXmtFrames_Type=Counter32
_HpDMAPrevXmtFrames_Object=MibScalar
hpDMAPrevXmtFrames=_HpDMAPrevXmtFrames_Object((1,3,6,1,4,1,11,2,14,11,5,1,2,2,12),_HpDMAPrevXmtFrames_Type())
hpDMAPrevXmtFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:hpDMAPrevXmtFrames.setStatus(_A)
_HpDMAFrameXmtPerSec_Type=Counter32
_HpDMAFrameXmtPerSec_Object=MibScalar
hpDMAFrameXmtPerSec=_HpDMAFrameXmtPerSec_Object((1,3,6,1,4,1,11,2,14,11,5,1,2,2,13),_HpDMAFrameXmtPerSec_Type())
hpDMAFrameXmtPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:hpDMAFrameXmtPerSec.setStatus(_A)
_HpDMAPeakXmtFrames_Type=Counter32
_HpDMAPeakXmtFrames_Object=MibScalar
hpDMAPeakXmtFrames=_HpDMAPeakXmtFrames_Object((1,3,6,1,4,1,11,2,14,11,5,1,2,2,14),_HpDMAPeakXmtFrames_Type())
hpDMAPeakXmtFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:hpDMAPeakXmtFrames.setStatus(_A)
_HpDMAPrevXmtOctets_Type=Counter32
_HpDMAPrevXmtOctets_Object=MibScalar
hpDMAPrevXmtOctets=_HpDMAPrevXmtOctets_Object((1,3,6,1,4,1,11,2,14,11,5,1,2,2,15),_HpDMAPrevXmtOctets_Type())
hpDMAPrevXmtOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:hpDMAPrevXmtOctets.setStatus(_A)
_HpDMAOctetsXmtPerSec_Type=Counter32
_HpDMAOctetsXmtPerSec_Object=MibScalar
hpDMAOctetsXmtPerSec=_HpDMAOctetsXmtPerSec_Object((1,3,6,1,4,1,11,2,14,11,5,1,2,2,16),_HpDMAOctetsXmtPerSec_Type())
hpDMAOctetsXmtPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:hpDMAOctetsXmtPerSec.setStatus(_A)
_HpDMAPeakXmtOctets_Type=Counter32
_HpDMAPeakXmtOctets_Object=MibScalar
hpDMAPeakXmtOctets=_HpDMAPeakXmtOctets_Object((1,3,6,1,4,1,11,2,14,11,5,1,2,2,17),_HpDMAPeakXmtOctets_Type())
hpDMAPeakXmtOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:hpDMAPeakXmtOctets.setStatus(_A)
_HpDMAFrameClippedcnt_Type=Counter32
_HpDMAFrameClippedcnt_Object=MibScalar
hpDMAFrameClippedcnt=_HpDMAFrameClippedcnt_Object((1,3,6,1,4,1,11,2,14,11,5,1,2,2,18),_HpDMAFrameClippedcnt_Type())
hpDMAFrameClippedcnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpDMAFrameClippedcnt.setStatus(_A)
_HpDMAFrameClippedOccurance_Type=Counter32
_HpDMAFrameClippedOccurance_Object=MibScalar
hpDMAFrameClippedOccurance=_HpDMAFrameClippedOccurance_Object((1,3,6,1,4,1,11,2,14,11,5,1,2,2,19),_HpDMAFrameClippedOccurance_Type())
hpDMAFrameClippedOccurance.setMaxAccess(_B)
if mibBuilder.loadTexts:hpDMAFrameClippedOccurance.setStatus(_A)
_HpDMAMissBufCnt_Type=Counter32
_HpDMAMissBufCnt_Object=MibScalar
hpDMAMissBufCnt=_HpDMAMissBufCnt_Object((1,3,6,1,4,1,11,2,14,11,5,1,2,2,20),_HpDMAMissBufCnt_Type())
hpDMAMissBufCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpDMAMissBufCnt.setStatus(_A)
mibBuilder.exportSymbols('NETSWITCH-DMA-MIB',**{'hp':hp,'nm':nm,'icf':icf,'hpicfObjects':hpicfObjects,'hpicfSwitch':hpicfSwitch,'hpSwitch':hpSwitch,'hpOpSystem':hpOpSystem,'hpHwSystem':hpHwSystem,'hpDMAStats':hpDMAStats,'hpDMAReset':hpDMAReset,'hpDMAFrameRcvcnt':hpDMAFrameRcvcnt,'hpDMAOctetsRcvcnt':hpDMAOctetsRcvcnt,'hpDMAPrevRcvFrames':hpDMAPrevRcvFrames,'hpDMAFrameRcvPerSec':hpDMAFrameRcvPerSec,'hpDMAPeakRcvFrames':hpDMAPeakRcvFrames,'hpDMAPrevRcvOctets':hpDMAPrevRcvOctets,'hpDMAOctetsRcvPerSec':hpDMAOctetsRcvPerSec,'hpDMAPeakRcvOctets':hpDMAPeakRcvOctets,'hpDMAFrameXmtcnt':hpDMAFrameXmtcnt,'hpDMAOctetsXmtcnt':hpDMAOctetsXmtcnt,'hpDMAPrevXmtFrames':hpDMAPrevXmtFrames,'hpDMAFrameXmtPerSec':hpDMAFrameXmtPerSec,'hpDMAPeakXmtFrames':hpDMAPeakXmtFrames,'hpDMAPrevXmtOctets':hpDMAPrevXmtOctets,'hpDMAOctetsXmtPerSec':hpDMAOctetsXmtPerSec,'hpDMAPeakXmtOctets':hpDMAPeakXmtOctets,'hpDMAFrameClippedcnt':hpDMAFrameClippedcnt,'hpDMAFrameClippedOccurance':hpDMAFrameClippedOccurance,'hpDMAMissBufCnt':hpDMAMissBufCnt})