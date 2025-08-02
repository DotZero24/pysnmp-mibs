_b='normal'
_a='localFrx'
_Z='briteCard6'
_Y='briteCard5'
_X='briteCard4'
_W='briteCard3'
_V='briteCard2'
_U='briteCard1'
_T='frxPvcIndex'
_S='frameRelay'
_R='use144kbps'
_Q='use128kbps'
_P='use64kbps'
_O='use56kbps'
_N='NotificationType'
_M='frxPAddrIndex'
_L='annexD'
_K='inactive'
_J='active'
_I='frxPortIndex'
_H='DisplayString'
_G='frxChUIndex'
_F='frxBankIndex'
_E='Cisco90Series-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier',_N,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_N,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
_CiscoTelesend_ObjectIdentity=ObjectIdentity
ciscoTelesend=_CiscoTelesend_ObjectIdentity((1,3,6,1,4,1,1570))
_FrMux_ObjectIdentity=ObjectIdentity
frMux=_FrMux_ObjectIdentity((1,3,6,1,4,1,1570,1))
_FrxSys_ObjectIdentity=ObjectIdentity
frxSys=_FrxSys_ObjectIdentity((1,3,6,1,4,1,1570,1,1))
class _FrxSysDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FrxSysDescr_Type.__name__=_H
_FrxSysDescr_Object=MibScalar
frxSysDescr=_FrxSysDescr_Object((1,3,6,1,4,1,1570,1,1,1),_FrxSysDescr_Type())
frxSysDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:frxSysDescr.setStatus(_A)
class _FrxClockHour_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_FrxClockHour_Type.__name__=_B
_FrxClockHour_Object=MibScalar
frxClockHour=_FrxClockHour_Object((1,3,6,1,4,1,1570,1,1,2),_FrxClockHour_Type())
frxClockHour.setMaxAccess(_D)
if mibBuilder.loadTexts:frxClockHour.setStatus(_A)
class _FrxClockMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_FrxClockMin_Type.__name__=_B
_FrxClockMin_Object=MibScalar
frxClockMin=_FrxClockMin_Object((1,3,6,1,4,1,1570,1,1,3),_FrxClockMin_Type())
frxClockMin.setMaxAccess(_D)
if mibBuilder.loadTexts:frxClockMin.setStatus(_A)
class _FrxClockSec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_FrxClockSec_Type.__name__=_B
_FrxClockSec_Object=MibScalar
frxClockSec=_FrxClockSec_Object((1,3,6,1,4,1,1570,1,1,4),_FrxClockSec_Type())
frxClockSec.setMaxAccess(_D)
if mibBuilder.loadTexts:frxClockSec.setStatus(_A)
_FrxUpTime_Type=TimeTicks
_FrxUpTime_Object=MibScalar
frxUpTime=_FrxUpTime_Object((1,3,6,1,4,1,1570,1,1,5),_FrxUpTime_Type())
frxUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:frxUpTime.setStatus(_A)
class _FrxAdminContact_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FrxAdminContact_Type.__name__=_H
_FrxAdminContact_Object=MibScalar
frxAdminContact=_FrxAdminContact_Object((1,3,6,1,4,1,1570,1,1,6),_FrxAdminContact_Type())
frxAdminContact.setMaxAccess(_D)
if mibBuilder.loadTexts:frxAdminContact.setStatus(_A)
class _FrxSysName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FrxSysName_Type.__name__=_H
_FrxSysName_Object=MibScalar
frxSysName=_FrxSysName_Object((1,3,6,1,4,1,1570,1,1,7),_FrxSysName_Type())
frxSysName.setMaxAccess(_D)
if mibBuilder.loadTexts:frxSysName.setStatus(_A)
class _FrxSysLoc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FrxSysLoc_Type.__name__=_H
_FrxSysLoc_Object=MibScalar
frxSysLoc=_FrxSysLoc_Object((1,3,6,1,4,1,1570,1,1,8),_FrxSysLoc_Type())
frxSysLoc.setMaxAccess(_D)
if mibBuilder.loadTexts:frxSysLoc.setStatus(_A)
class _FrxSysVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FrxSysVersion_Type.__name__=_B
_FrxSysVersion_Object=MibScalar
frxSysVersion=_FrxSysVersion_Object((1,3,6,1,4,1,1570,1,1,9),_FrxSysVersion_Type())
frxSysVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:frxSysVersion.setStatus(_A)
class _FrxUPerfTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enableUPerfTrap',1),('disableUPerfTrap',2)))
_FrxUPerfTrapEnable_Type.__name__=_B
_FrxUPerfTrapEnable_Object=MibScalar
frxUPerfTrapEnable=_FrxUPerfTrapEnable_Object((1,3,6,1,4,1,1570,1,1,10),_FrxUPerfTrapEnable_Type())
frxUPerfTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:frxUPerfTrapEnable.setStatus(_A)
_FrxAgtLinkErrors_Type=Counter32
_FrxAgtLinkErrors_Object=MibScalar
frxAgtLinkErrors=_FrxAgtLinkErrors_Object((1,3,6,1,4,1,1570,1,1,11),_FrxAgtLinkErrors_Type())
frxAgtLinkErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:frxAgtLinkErrors.setStatus(_A)
_FrxAgtProtErrors_Type=Counter32
_FrxAgtProtErrors_Object=MibScalar
frxAgtProtErrors=_FrxAgtProtErrors_Object((1,3,6,1,4,1,1570,1,1,12),_FrxAgtProtErrors_Type())
frxAgtProtErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:frxAgtProtErrors.setStatus(_A)
_FrxAgtChInactive_Type=Counter32
_FrxAgtChInactive_Object=MibScalar
frxAgtChInactive=_FrxAgtChInactive_Object((1,3,6,1,4,1,1570,1,1,13),_FrxAgtChInactive_Type())
frxAgtChInactive.setMaxAccess(_C)
if mibBuilder.loadTexts:frxAgtChInactive.setStatus(_A)
class _FrxAgtChStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_FrxAgtChStatus_Type.__name__=_B
_FrxAgtChStatus_Object=MibScalar
frxAgtChStatus=_FrxAgtChStatus_Object((1,3,6,1,4,1,1570,1,1,14),_FrxAgtChStatus_Type())
frxAgtChStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:frxAgtChStatus.setStatus(_A)
_FrxDefault_ObjectIdentity=ObjectIdentity
frxDefault=_FrxDefault_ObjectIdentity((1,3,6,1,4,1,1570,1,2))
class _FrxDefaultEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enableAutoLoad',1),('disableAutoLoad',2)))
_FrxDefaultEnable_Type.__name__=_B
_FrxDefaultEnable_Object=MibScalar
frxDefaultEnable=_FrxDefaultEnable_Object((1,3,6,1,4,1,1570,1,2,1),_FrxDefaultEnable_Type())
frxDefaultEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:frxDefaultEnable.setStatus(_A)
class _FrxDefaultTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enableConfigureTrap',1),('disableConfigureTrap',2)))
_FrxDefaultTrap_Type.__name__=_B
_FrxDefaultTrap_Object=MibScalar
frxDefaultTrap=_FrxDefaultTrap_Object((1,3,6,1,4,1,1570,1,2,2),_FrxDefaultTrap_Type())
frxDefaultTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:frxDefaultTrap.setStatus(_A)
class _FrxDConfigSrc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('snmp',2)))
_FrxDConfigSrc_Type.__name__=_B
_FrxDConfigSrc_Object=MibScalar
frxDConfigSrc=_FrxDConfigSrc_Object((1,3,6,1,4,1,1570,1,2,3),_FrxDConfigSrc_Type())
frxDConfigSrc.setMaxAccess(_D)
if mibBuilder.loadTexts:frxDConfigSrc.setStatus(_A)
class _FrxDMgtT391_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_FrxDMgtT391_Type.__name__=_B
_FrxDMgtT391_Object=MibScalar
frxDMgtT391=_FrxDMgtT391_Object((1,3,6,1,4,1,1570,1,2,4),_FrxDMgtT391_Type())
frxDMgtT391.setMaxAccess(_D)
if mibBuilder.loadTexts:frxDMgtT391.setStatus(_A)
class _FrxDMgtT392_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_FrxDMgtT392_Type.__name__=_B
_FrxDMgtT392_Object=MibScalar
frxDMgtT392=_FrxDMgtT392_Object((1,3,6,1,4,1,1570,1,2,5),_FrxDMgtT392_Type())
frxDMgtT392.setMaxAccess(_D)
if mibBuilder.loadTexts:frxDMgtT392.setStatus(_A)
class _FrxDMgtN391_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FrxDMgtN391_Type.__name__=_B
_FrxDMgtN391_Object=MibScalar
frxDMgtN391=_FrxDMgtN391_Object((1,3,6,1,4,1,1570,1,2,6),_FrxDMgtN391_Type())
frxDMgtN391.setMaxAccess(_D)
if mibBuilder.loadTexts:frxDMgtN391.setStatus(_A)
class _FrxDMgtN392_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FrxDMgtN392_Type.__name__=_B
_FrxDMgtN392_Object=MibScalar
frxDMgtN392=_FrxDMgtN392_Object((1,3,6,1,4,1,1570,1,2,7),_FrxDMgtN392_Type())
frxDMgtN392.setMaxAccess(_D)
if mibBuilder.loadTexts:frxDMgtN392.setStatus(_A)
class _FrxDMgtN393_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FrxDMgtN393_Type.__name__=_B
_FrxDMgtN393_Object=MibScalar
frxDMgtN393=_FrxDMgtN393_Object((1,3,6,1,4,1,1570,1,2,8),_FrxDMgtN393_Type())
frxDMgtN393.setMaxAccess(_D)
if mibBuilder.loadTexts:frxDMgtN393.setStatus(_A)
class _FrxDPortSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_R,4)))
_FrxDPortSpeed_Type.__name__=_B
_FrxDPortSpeed_Object=MibScalar
frxDPortSpeed=_FrxDPortSpeed_Object((1,3,6,1,4,1,1570,1,2,9),_FrxDPortSpeed_Type())
frxDPortSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:frxDPortSpeed.setStatus(_A)
class _FrxDPortProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),('ppp',2)))
_FrxDPortProtocol_Type.__name__=_B
_FrxDPortProtocol_Object=MibScalar
frxDPortProtocol=_FrxDPortProtocol_Object((1,3,6,1,4,1,1570,1,2,10),_FrxDPortProtocol_Type())
frxDPortProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:frxDPortProtocol.setStatus(_A)
class _FrxDCktCIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1544000))
_FrxDCktCIR_Type.__name__=_B
_FrxDCktCIR_Object=MibScalar
frxDCktCIR=_FrxDCktCIR_Object((1,3,6,1,4,1,1570,1,2,11),_FrxDCktCIR_Type())
frxDCktCIR.setMaxAccess(_D)
if mibBuilder.loadTexts:frxDCktCIR.setStatus(_A)
class _FrxDCktBc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_FrxDCktBc_Type.__name__=_B
_FrxDCktBc_Object=MibScalar
frxDCktBc=_FrxDCktBc_Object((1,3,6,1,4,1,1570,1,2,12),_FrxDCktBc_Type())
frxDCktBc.setMaxAccess(_D)
if mibBuilder.loadTexts:frxDCktBc.setStatus(_A)
class _FrxDCktBe_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777212))
_FrxDCktBe_Type.__name__=_B
_FrxDCktBe_Object=MibScalar
frxDCktBe=_FrxDCktBe_Object((1,3,6,1,4,1,1570,1,2,13),_FrxDCktBe_Type())
frxDCktBe.setMaxAccess(_D)
if mibBuilder.loadTexts:frxDCktBe.setStatus(_A)
_FrxBank_ObjectIdentity=ObjectIdentity
frxBank=_FrxBank_ObjectIdentity((1,3,6,1,4,1,1570,1,3))
_FrxBankTable_Object=MibTable
frxBankTable=_FrxBankTable_Object((1,3,6,1,4,1,1570,1,3,1))
if mibBuilder.loadTexts:frxBankTable.setStatus(_A)
_FrxBankEntry_Object=MibTableRow
frxBankEntry=_FrxBankEntry_Object((1,3,6,1,4,1,1570,1,3,1,1))
frxBankEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:frxBankEntry.setStatus(_A)
class _FrxBankIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1007))
_FrxBankIndex_Type.__name__=_B
_FrxBankIndex_Object=MibTableColumn
frxBankIndex=_FrxBankIndex_Object((1,3,6,1,4,1,1570,1,3,1,1,1),_FrxBankIndex_Type())
frxBankIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:frxBankIndex.setStatus(_A)
class _FrxBankType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('d4',1))
_FrxBankType_Type.__name__=_B
_FrxBankType_Object=MibTableColumn
frxBankType=_FrxBankType_Object((1,3,6,1,4,1,1570,1,3,1,1,2),_FrxBankType_Type())
frxBankType.setMaxAccess(_D)
if mibBuilder.loadTexts:frxBankType.setStatus(_A)
_FrxChUnit_ObjectIdentity=ObjectIdentity
frxChUnit=_FrxChUnit_ObjectIdentity((1,3,6,1,4,1,1570,1,4))
_FrxChUTable_Object=MibTable
frxChUTable=_FrxChUTable_Object((1,3,6,1,4,1,1570,1,4,1))
if mibBuilder.loadTexts:frxChUTable.setStatus(_A)
_FrxChUEntry_Object=MibTableRow
frxChUEntry=_FrxChUEntry_Object((1,3,6,1,4,1,1570,1,4,1,1))
frxChUEntry.setIndexNames((0,_E,_F),(0,_E,_G))
if mibBuilder.loadTexts:frxChUEntry.setStatus(_A)
class _FrxChUIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_FrxChUIndex_Type.__name__=_B
_FrxChUIndex_Object=MibTableColumn
frxChUIndex=_FrxChUIndex_Object((1,3,6,1,4,1,1570,1,4,1,1,1),_FrxChUIndex_Type())
frxChUIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:frxChUIndex.setStatus(_A)
class _FrxChUType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(100));namedValues=NamedValues(('cisco90i',100))
_FrxChUType_Type.__name__=_B
_FrxChUType_Object=MibTableColumn
frxChUType=_FrxChUType_Object((1,3,6,1,4,1,1570,1,4,1,1,2),_FrxChUType_Type())
frxChUType.setMaxAccess(_C)
if mibBuilder.loadTexts:frxChUType.setStatus(_A)
class _FrxChUVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FrxChUVersion_Type.__name__=_B
_FrxChUVersion_Object=MibTableColumn
frxChUVersion=_FrxChUVersion_Object((1,3,6,1,4,1,1570,1,4,1,1,3),_FrxChUVersion_Type())
frxChUVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:frxChUVersion.setStatus(_A)
class _FrxSigProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_L,1))
_FrxSigProtocol_Type.__name__=_B
_FrxSigProtocol_Object=MibTableColumn
frxSigProtocol=_FrxSigProtocol_Object((1,3,6,1,4,1,1570,1,4,1,1,4),_FrxSigProtocol_Type())
frxSigProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:frxSigProtocol.setStatus(_A)
class _FrxConfigSrc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('snmp',2)))
_FrxConfigSrc_Type.__name__=_B
_FrxConfigSrc_Object=MibTableColumn
frxConfigSrc=_FrxConfigSrc_Object((1,3,6,1,4,1,1570,1,4,1,1,5),_FrxConfigSrc_Type())
frxConfigSrc.setMaxAccess(_D)
if mibBuilder.loadTexts:frxConfigSrc.setStatus(_A)
class _FrxDLCIAdLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('twoOctetDlci',1))
_FrxDLCIAdLen_Type.__name__=_B
_FrxDLCIAdLen_Object=MibTableColumn
frxDLCIAdLen=_FrxDLCIAdLen_Object((1,3,6,1,4,1,1570,1,4,1,1,6),_FrxDLCIAdLen_Type())
frxDLCIAdLen.setMaxAccess(_C)
if mibBuilder.loadTexts:frxDLCIAdLen.setStatus(_A)
_FrxNetInOctets_Type=Counter32
_FrxNetInOctets_Object=MibTableColumn
frxNetInOctets=_FrxNetInOctets_Object((1,3,6,1,4,1,1570,1,4,1,1,7),_FrxNetInOctets_Type())
frxNetInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:frxNetInOctets.setStatus(_A)
_FrxNetOutOctets_Type=Counter32
_FrxNetOutOctets_Object=MibTableColumn
frxNetOutOctets=_FrxNetOutOctets_Object((1,3,6,1,4,1,1570,1,4,1,1,8),_FrxNetOutOctets_Type())
frxNetOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:frxNetOutOctets.setStatus(_A)
_FrxNetBadFrames_Type=Counter32
_FrxNetBadFrames_Object=MibTableColumn
frxNetBadFrames=_FrxNetBadFrames_Object((1,3,6,1,4,1,1570,1,4,1,1,9),_FrxNetBadFrames_Type())
frxNetBadFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:frxNetBadFrames.setStatus(_A)
_FrxNetHDLCEs_Type=Counter32
_FrxNetHDLCEs_Object=MibTableColumn
frxNetHDLCEs=_FrxNetHDLCEs_Object((1,3,6,1,4,1,1570,1,4,1,1,10),_FrxNetHDLCEs_Type())
frxNetHDLCEs.setMaxAccess(_C)
if mibBuilder.loadTexts:frxNetHDLCEs.setStatus(_A)
_FrxNetCRCEs_Type=Counter32
_FrxNetCRCEs_Object=MibTableColumn
frxNetCRCEs=_FrxNetCRCEs_Object((1,3,6,1,4,1,1570,1,4,1,1,11),_FrxNetCRCEs_Type())
frxNetCRCEs.setMaxAccess(_C)
if mibBuilder.loadTexts:frxNetCRCEs.setStatus(_A)
_FrxNetLinkEs_Type=Counter32
_FrxNetLinkEs_Object=MibTableColumn
frxNetLinkEs=_FrxNetLinkEs_Object((1,3,6,1,4,1,1570,1,4,1,1,12),_FrxNetLinkEs_Type())
frxNetLinkEs.setMaxAccess(_C)
if mibBuilder.loadTexts:frxNetLinkEs.setStatus(_A)
_FrxNetFrShEs_Type=Counter32
_FrxNetFrShEs_Object=MibTableColumn
frxNetFrShEs=_FrxNetFrShEs_Object((1,3,6,1,4,1,1570,1,4,1,1,13),_FrxNetFrShEs_Type())
frxNetFrShEs.setMaxAccess(_C)
if mibBuilder.loadTexts:frxNetFrShEs.setStatus(_A)
_FrxNetFrLgEs_Type=Counter32
_FrxNetFrLgEs_Object=MibTableColumn
frxNetFrLgEs=_FrxNetFrLgEs_Object((1,3,6,1,4,1,1570,1,4,1,1,14),_FrxNetFrLgEs_Type())
frxNetFrLgEs.setMaxAccess(_C)
if mibBuilder.loadTexts:frxNetFrLgEs.setStatus(_A)
_FrxNetPPPEs_Type=Counter32
_FrxNetPPPEs_Object=MibTableColumn
frxNetPPPEs=_FrxNetPPPEs_Object((1,3,6,1,4,1,1570,1,4,1,1,15),_FrxNetPPPEs_Type())
frxNetPPPEs.setMaxAccess(_C)
if mibBuilder.loadTexts:frxNetPPPEs.setStatus(_A)
_FrxNetBufEs_Type=Counter32
_FrxNetBufEs_Object=MibTableColumn
frxNetBufEs=_FrxNetBufEs_Object((1,3,6,1,4,1,1570,1,4,1,1,16),_FrxNetBufEs_Type())
frxNetBufEs.setMaxAccess(_C)
if mibBuilder.loadTexts:frxNetBufEs.setStatus(_A)
_FrxMgt_ObjectIdentity=ObjectIdentity
frxMgt=_FrxMgt_ObjectIdentity((1,3,6,1,4,1,1570,1,5))
_FrxMgtTable_Object=MibTable
frxMgtTable=_FrxMgtTable_Object((1,3,6,1,4,1,1570,1,5,1))
if mibBuilder.loadTexts:frxMgtTable.setStatus(_A)
_FrxMgtEntry_Object=MibTableRow
frxMgtEntry=_FrxMgtEntry_Object((1,3,6,1,4,1,1570,1,5,1,1))
frxMgtEntry.setIndexNames((0,_E,_F),(0,_E,_G))
if mibBuilder.loadTexts:frxMgtEntry.setStatus(_A)
class _FrxPortsInSvc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_FrxPortsInSvc_Type.__name__=_B
_FrxPortsInSvc_Object=MibTableColumn
frxPortsInSvc=_FrxPortsInSvc_Object((1,3,6,1,4,1,1570,1,5,1,1,1),_FrxPortsInSvc_Type())
frxPortsInSvc.setMaxAccess(_C)
if mibBuilder.loadTexts:frxPortsInSvc.setStatus(_A)
class _FrxMgtT391_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_FrxMgtT391_Type.__name__=_B
_FrxMgtT391_Object=MibTableColumn
frxMgtT391=_FrxMgtT391_Object((1,3,6,1,4,1,1570,1,5,1,1,2),_FrxMgtT391_Type())
frxMgtT391.setMaxAccess(_D)
if mibBuilder.loadTexts:frxMgtT391.setStatus(_A)
class _FrxMgtT392_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_FrxMgtT392_Type.__name__=_B
_FrxMgtT392_Object=MibTableColumn
frxMgtT392=_FrxMgtT392_Object((1,3,6,1,4,1,1570,1,5,1,1,3),_FrxMgtT392_Type())
frxMgtT392.setMaxAccess(_D)
if mibBuilder.loadTexts:frxMgtT392.setStatus(_A)
class _FrxMgtN391_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FrxMgtN391_Type.__name__=_B
_FrxMgtN391_Object=MibTableColumn
frxMgtN391=_FrxMgtN391_Object((1,3,6,1,4,1,1570,1,5,1,1,4),_FrxMgtN391_Type())
frxMgtN391.setMaxAccess(_D)
if mibBuilder.loadTexts:frxMgtN391.setStatus(_A)
class _FrxMgtN392_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FrxMgtN392_Type.__name__=_B
_FrxMgtN392_Object=MibTableColumn
frxMgtN392=_FrxMgtN392_Object((1,3,6,1,4,1,1570,1,5,1,1,5),_FrxMgtN392_Type())
frxMgtN392.setMaxAccess(_D)
if mibBuilder.loadTexts:frxMgtN392.setStatus(_A)
class _FrxMgtN393_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FrxMgtN393_Type.__name__=_B
_FrxMgtN393_Object=MibTableColumn
frxMgtN393=_FrxMgtN393_Object((1,3,6,1,4,1,1570,1,5,1,1,6),_FrxMgtN393_Type())
frxMgtN393.setMaxAccess(_D)
if mibBuilder.loadTexts:frxMgtN393.setStatus(_A)
_FrxNetLinkErrors_Type=Counter32
_FrxNetLinkErrors_Object=MibTableColumn
frxNetLinkErrors=_FrxNetLinkErrors_Object((1,3,6,1,4,1,1570,1,5,1,1,7),_FrxNetLinkErrors_Type())
frxNetLinkErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:frxNetLinkErrors.setStatus(_A)
_FrxNetProtErrors_Type=Counter32
_FrxNetProtErrors_Object=MibTableColumn
frxNetProtErrors=_FrxNetProtErrors_Object((1,3,6,1,4,1,1570,1,5,1,1,8),_FrxNetProtErrors_Type())
frxNetProtErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:frxNetProtErrors.setStatus(_A)
_FrxNetChInactive_Type=Counter32
_FrxNetChInactive_Object=MibTableColumn
frxNetChInactive=_FrxNetChInactive_Object((1,3,6,1,4,1,1570,1,5,1,1,9),_FrxNetChInactive_Type())
frxNetChInactive.setMaxAccess(_C)
if mibBuilder.loadTexts:frxNetChInactive.setStatus(_A)
class _FrxNetChStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_FrxNetChStatus_Type.__name__=_B
_FrxNetChStatus_Object=MibTableColumn
frxNetChStatus=_FrxNetChStatus_Object((1,3,6,1,4,1,1570,1,5,1,1,10),_FrxNetChStatus_Type())
frxNetChStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:frxNetChStatus.setStatus(_A)
_FrxMgtPortTable_Object=MibTable
frxMgtPortTable=_FrxMgtPortTable_Object((1,3,6,1,4,1,1570,1,5,2))
if mibBuilder.loadTexts:frxMgtPortTable.setStatus(_A)
_FrxMgtPortEntry_Object=MibTableRow
frxMgtPortEntry=_FrxMgtPortEntry_Object((1,3,6,1,4,1,1570,1,5,2,1))
frxMgtPortEntry.setIndexNames((0,_E,_F),(0,_E,_G),(0,_E,_I))
if mibBuilder.loadTexts:frxMgtPortEntry.setStatus(_A)
class _FrxPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_FrxPortIndex_Type.__name__=_B
_FrxPortIndex_Object=MibTableColumn
frxPortIndex=_FrxPortIndex_Object((1,3,6,1,4,1,1570,1,5,2,1,1),_FrxPortIndex_Type())
frxPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:frxPortIndex.setStatus(_A)
_FrxPortLinkErrors_Type=Counter32
_FrxPortLinkErrors_Object=MibTableColumn
frxPortLinkErrors=_FrxPortLinkErrors_Object((1,3,6,1,4,1,1570,1,5,2,1,2),_FrxPortLinkErrors_Type())
frxPortLinkErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:frxPortLinkErrors.setStatus(_A)
_FrxPortProtErrors_Type=Counter32
_FrxPortProtErrors_Object=MibTableColumn
frxPortProtErrors=_FrxPortProtErrors_Object((1,3,6,1,4,1,1570,1,5,2,1,3),_FrxPortProtErrors_Type())
frxPortProtErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:frxPortProtErrors.setStatus(_A)
_FrxPortChInactive_Type=Counter32
_FrxPortChInactive_Object=MibTableColumn
frxPortChInactive=_FrxPortChInactive_Object((1,3,6,1,4,1,1570,1,5,2,1,4),_FrxPortChInactive_Type())
frxPortChInactive.setMaxAccess(_C)
if mibBuilder.loadTexts:frxPortChInactive.setStatus(_A)
_FrxPort_ObjectIdentity=ObjectIdentity
frxPort=_FrxPort_ObjectIdentity((1,3,6,1,4,1,1570,1,6))
_FrxPortTable_Object=MibTable
frxPortTable=_FrxPortTable_Object((1,3,6,1,4,1,1570,1,6,1))
if mibBuilder.loadTexts:frxPortTable.setStatus(_A)
_FrxPortEntry_Object=MibTableRow
frxPortEntry=_FrxPortEntry_Object((1,3,6,1,4,1,1570,1,6,1,1))
frxPortEntry.setIndexNames((0,_E,_F),(0,_E,_G),(0,_E,_I))
if mibBuilder.loadTexts:frxPortEntry.setStatus(_A)
class _FrxPortSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_R,4)))
_FrxPortSpeed_Type.__name__=_B
_FrxPortSpeed_Object=MibTableColumn
frxPortSpeed=_FrxPortSpeed_Object((1,3,6,1,4,1,1570,1,6,1,1,1),_FrxPortSpeed_Type())
frxPortSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:frxPortSpeed.setStatus(_A)
class _FrxPortProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),('ppp',2)))
_FrxPortProtocol_Type.__name__=_B
_FrxPortProtocol_Object=MibTableColumn
frxPortProtocol=_FrxPortProtocol_Object((1,3,6,1,4,1,1570,1,6,1,1,2),_FrxPortProtocol_Type())
frxPortProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:frxPortProtocol.setStatus(_A)
class _FrxDSLStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('loopDown',1),('dslSyncOnly',2),('loopUpInactive',3),('loopUp',4)))
_FrxDSLStatus_Type.__name__=_B
_FrxDSLStatus_Object=MibTableColumn
frxDSLStatus=_FrxDSLStatus_Object((1,3,6,1,4,1,1570,1,6,1,1,3),_FrxDSLStatus_Type())
frxDSLStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:frxDSLStatus.setStatus(_A)
class _FrxPVCAssigned_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_FrxPVCAssigned_Type.__name__=_B
_FrxPVCAssigned_Object=MibTableColumn
frxPVCAssigned=_FrxPVCAssigned_Object((1,3,6,1,4,1,1570,1,6,1,1,4),_FrxPVCAssigned_Type())
frxPVCAssigned.setMaxAccess(_C)
if mibBuilder.loadTexts:frxPVCAssigned.setStatus(_A)
_FrxLastChange_Type=TimeTicks
_FrxLastChange_Object=MibTableColumn
frxLastChange=_FrxLastChange_Object((1,3,6,1,4,1,1570,1,6,1,1,5),_FrxLastChange_Type())
frxLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:frxLastChange.setStatus(_A)
class _FrxBrite_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_FrxBrite_Type.__name__=_B
_FrxBrite_Object=MibTableColumn
frxBrite=_FrxBrite_Object((1,3,6,1,4,1,1570,1,6,1,1,6),_FrxBrite_Type())
frxBrite.setMaxAccess(_C)
if mibBuilder.loadTexts:frxBrite.setStatus(_A)
_FrxDSLInOctets_Type=Counter32
_FrxDSLInOctets_Object=MibTableColumn
frxDSLInOctets=_FrxDSLInOctets_Object((1,3,6,1,4,1,1570,1,6,1,1,7),_FrxDSLInOctets_Type())
frxDSLInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:frxDSLInOctets.setStatus(_A)
_FrxDSLOutOctets_Type=Counter32
_FrxDSLOutOctets_Object=MibTableColumn
frxDSLOutOctets=_FrxDSLOutOctets_Object((1,3,6,1,4,1,1570,1,6,1,1,8),_FrxDSLOutOctets_Type())
frxDSLOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:frxDSLOutOctets.setStatus(_A)
_FrxT1InOctets_Type=Counter32
_FrxT1InOctets_Object=MibTableColumn
frxT1InOctets=_FrxT1InOctets_Object((1,3,6,1,4,1,1570,1,6,1,1,9),_FrxT1InOctets_Type())
frxT1InOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:frxT1InOctets.setStatus(_A)
_FrxT1OutOctets_Type=Counter32
_FrxT1OutOctets_Object=MibTableColumn
frxT1OutOctets=_FrxT1OutOctets_Object((1,3,6,1,4,1,1570,1,6,1,1,10),_FrxT1OutOctets_Type())
frxT1OutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:frxT1OutOctets.setStatus(_A)
_FrxDSLBadFrames_Type=Counter32
_FrxDSLBadFrames_Object=MibTableColumn
frxDSLBadFrames=_FrxDSLBadFrames_Object((1,3,6,1,4,1,1570,1,6,1,1,11),_FrxDSLBadFrames_Type())
frxDSLBadFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:frxDSLBadFrames.setStatus(_A)
_FrxDSLHDLCEs_Type=Counter32
_FrxDSLHDLCEs_Object=MibTableColumn
frxDSLHDLCEs=_FrxDSLHDLCEs_Object((1,3,6,1,4,1,1570,1,6,1,1,12),_FrxDSLHDLCEs_Type())
frxDSLHDLCEs.setMaxAccess(_C)
if mibBuilder.loadTexts:frxDSLHDLCEs.setStatus(_A)
_FrxDSLCRCEs_Type=Counter32
_FrxDSLCRCEs_Object=MibTableColumn
frxDSLCRCEs=_FrxDSLCRCEs_Object((1,3,6,1,4,1,1570,1,6,1,1,13),_FrxDSLCRCEs_Type())
frxDSLCRCEs.setMaxAccess(_C)
if mibBuilder.loadTexts:frxDSLCRCEs.setStatus(_A)
_FrxDSLLinkEs_Type=Counter32
_FrxDSLLinkEs_Object=MibTableColumn
frxDSLLinkEs=_FrxDSLLinkEs_Object((1,3,6,1,4,1,1570,1,6,1,1,14),_FrxDSLLinkEs_Type())
frxDSLLinkEs.setMaxAccess(_C)
if mibBuilder.loadTexts:frxDSLLinkEs.setStatus(_A)
_FrxDSLFrShEs_Type=Counter32
_FrxDSLFrShEs_Object=MibTableColumn
frxDSLFrShEs=_FrxDSLFrShEs_Object((1,3,6,1,4,1,1570,1,6,1,1,15),_FrxDSLFrShEs_Type())
frxDSLFrShEs.setMaxAccess(_C)
if mibBuilder.loadTexts:frxDSLFrShEs.setStatus(_A)
_FrxDSLFrLgEs_Type=Counter32
_FrxDSLFrLgEs_Object=MibTableColumn
frxDSLFrLgEs=_FrxDSLFrLgEs_Object((1,3,6,1,4,1,1570,1,6,1,1,16),_FrxDSLFrLgEs_Type())
frxDSLFrLgEs.setMaxAccess(_C)
if mibBuilder.loadTexts:frxDSLFrLgEs.setStatus(_A)
_FrxDSLDLCIEs_Type=Counter32
_FrxDSLDLCIEs_Object=MibTableColumn
frxDSLDLCIEs=_FrxDSLDLCIEs_Object((1,3,6,1,4,1,1570,1,6,1,1,17),_FrxDSLDLCIEs_Type())
frxDSLDLCIEs.setMaxAccess(_C)
if mibBuilder.loadTexts:frxDSLDLCIEs.setStatus(_A)
class _FrxTxBuf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FrxTxBuf_Type.__name__=_B
_FrxTxBuf_Object=MibTableColumn
frxTxBuf=_FrxTxBuf_Object((1,3,6,1,4,1,1570,1,6,1,1,18),_FrxTxBuf_Type())
frxTxBuf.setMaxAccess(_C)
if mibBuilder.loadTexts:frxTxBuf.setStatus(_A)
class _FrxRxBuf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FrxRxBuf_Type.__name__=_B
_FrxRxBuf_Object=MibTableColumn
frxRxBuf=_FrxRxBuf_Object((1,3,6,1,4,1,1570,1,6,1,1,19),_FrxRxBuf_Type())
frxRxBuf.setMaxAccess(_C)
if mibBuilder.loadTexts:frxRxBuf.setStatus(_A)
_FrxPortNetEs_Type=Counter32
_FrxPortNetEs_Object=MibTableColumn
frxPortNetEs=_FrxPortNetEs_Object((1,3,6,1,4,1,1570,1,6,1,1,20),_FrxPortNetEs_Type())
frxPortNetEs.setMaxAccess(_C)
if mibBuilder.loadTexts:frxPortNetEs.setStatus(_A)
_FrxCircuitTable_Object=MibTable
frxCircuitTable=_FrxCircuitTable_Object((1,3,6,1,4,1,1570,1,6,2))
if mibBuilder.loadTexts:frxCircuitTable.setStatus(_A)
_FrxCircuitEntry_Object=MibTableRow
frxCircuitEntry=_FrxCircuitEntry_Object((1,3,6,1,4,1,1570,1,6,2,1))
frxCircuitEntry.setIndexNames((0,_E,_F),(0,_E,_G),(0,_E,_I),(0,_E,_T))
if mibBuilder.loadTexts:frxCircuitEntry.setStatus(_A)
class _FrxPvcIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,23))
_FrxPvcIndex_Type.__name__=_B
_FrxPvcIndex_Object=MibTableColumn
frxPvcIndex=_FrxPvcIndex_Object((1,3,6,1,4,1,1570,1,6,2,1,1),_FrxPvcIndex_Type())
frxPvcIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:frxPvcIndex.setStatus(_A)
class _FrxCktCIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1544000))
_FrxCktCIR_Type.__name__=_B
_FrxCktCIR_Object=MibTableColumn
frxCktCIR=_FrxCktCIR_Object((1,3,6,1,4,1,1570,1,6,2,1,2),_FrxCktCIR_Type())
frxCktCIR.setMaxAccess(_D)
if mibBuilder.loadTexts:frxCktCIR.setStatus(_A)
class _FrxCktBc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_FrxCktBc_Type.__name__=_B
_FrxCktBc_Object=MibTableColumn
frxCktBc=_FrxCktBc_Object((1,3,6,1,4,1,1570,1,6,2,1,3),_FrxCktBc_Type())
frxCktBc.setMaxAccess(_D)
if mibBuilder.loadTexts:frxCktBc.setStatus(_A)
class _FrxCktBe_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_FrxCktBe_Type.__name__=_B
_FrxCktBe_Object=MibTableColumn
frxCktBe=_FrxCktBe_Object((1,3,6,1,4,1,1570,1,6,2,1,4),_FrxCktBe_Type())
frxCktBe.setMaxAccess(_D)
if mibBuilder.loadTexts:frxCktBe.setStatus(_A)
class _FrxFarEndOpStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_FrxFarEndOpStat_Type.__name__=_B
_FrxFarEndOpStat_Object=MibTableColumn
frxFarEndOpStat=_FrxFarEndOpStat_Object((1,3,6,1,4,1,1570,1,6,2,1,5),_FrxFarEndOpStat_Type())
frxFarEndOpStat.setMaxAccess(_C)
if mibBuilder.loadTexts:frxFarEndOpStat.setStatus(_A)
_FrxCktInOctets_Type=Counter32
_FrxCktInOctets_Object=MibTableColumn
frxCktInOctets=_FrxCktInOctets_Object((1,3,6,1,4,1,1570,1,6,2,1,6),_FrxCktInOctets_Type())
frxCktInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:frxCktInOctets.setStatus(_A)
_FrxCktOutOctets_Type=Counter32
_FrxCktOutOctets_Object=MibTableColumn
frxCktOutOctets=_FrxCktOutOctets_Object((1,3,6,1,4,1,1570,1,6,2,1,7),_FrxCktOutOctets_Type())
frxCktOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:frxCktOutOctets.setStatus(_A)
_FrxCktInFrames_Type=Counter32
_FrxCktInFrames_Object=MibTableColumn
frxCktInFrames=_FrxCktInFrames_Object((1,3,6,1,4,1,1570,1,6,2,1,8),_FrxCktInFrames_Type())
frxCktInFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:frxCktInFrames.setStatus(_A)
_FrxCktOutFrames_Type=Counter32
_FrxCktOutFrames_Object=MibTableColumn
frxCktOutFrames=_FrxCktOutFrames_Object((1,3,6,1,4,1,1570,1,6,2,1,9),_FrxCktOutFrames_Type())
frxCktOutFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:frxCktOutFrames.setStatus(_A)
_FrxCktDiscards_Type=Counter32
_FrxCktDiscards_Object=MibTableColumn
frxCktDiscards=_FrxCktDiscards_Object((1,3,6,1,4,1,1570,1,6,2,1,10),_FrxCktDiscards_Type())
frxCktDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:frxCktDiscards.setStatus(_A)
_FrxUEocTable_Object=MibTable
frxUEocTable=_FrxUEocTable_Object((1,3,6,1,4,1,1570,1,6,3))
if mibBuilder.loadTexts:frxUEocTable.setStatus(_A)
_FrxUEocEntry_Object=MibTableRow
frxUEocEntry=_FrxUEocEntry_Object((1,3,6,1,4,1,1570,1,6,3,1))
frxUEocEntry.setIndexNames((0,_E,_F),(0,_E,_G))
if mibBuilder.loadTexts:frxUEocEntry.setStatus(_A)
class _FrxTestPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_FrxTestPort_Type.__name__=_B
_FrxTestPort_Object=MibTableColumn
frxTestPort=_FrxTestPort_Object((1,3,6,1,4,1,1570,1,6,3,1,1),_FrxTestPort_Type())
frxTestPort.setMaxAccess(_D)
if mibBuilder.loadTexts:frxTestPort.setStatus(_A)
class _FrxTestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('loopbackAndBert',1),('bertOnly',2),('sendCorruptCRC',3),('loopbackOnly',4),('localLoopAllPorts',5)))
_FrxTestType_Type.__name__=_B
_FrxTestType_Object=MibTableColumn
frxTestType=_FrxTestType_Object((1,3,6,1,4,1,1570,1,6,3,1,2),_FrxTestType_Type())
frxTestType.setMaxAccess(_D)
if mibBuilder.loadTexts:frxTestType.setStatus(_A)
class _FrxLoopLoc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_U,1),(_V,2),(_W,3),(_X,4),(_Y,5),(_Z,6),(_a,7),('nt1',8)))
_FrxLoopLoc_Type.__name__=_B
_FrxLoopLoc_Object=MibTableColumn
frxLoopLoc=_FrxLoopLoc_Object((1,3,6,1,4,1,1570,1,6,3,1,3),_FrxLoopLoc_Type())
frxLoopLoc.setMaxAccess(_D)
if mibBuilder.loadTexts:frxLoopLoc.setStatus(_A)
class _FrxLoopCh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('b1only',1),('b2only',2),('all',3)))
_FrxLoopCh_Type.__name__=_B
_FrxLoopCh_Object=MibTableColumn
frxLoopCh=_FrxLoopCh_Object((1,3,6,1,4,1,1570,1,6,3,1,4),_FrxLoopCh_Type())
frxLoopCh.setMaxAccess(_D)
if mibBuilder.loadTexts:frxLoopCh.setStatus(_A)
class _FrxStartTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stopTest',1),('startTest',2)))
_FrxStartTest_Type.__name__=_B
_FrxStartTest_Object=MibTableColumn
frxStartTest=_FrxStartTest_Object((1,3,6,1,4,1,1570,1,6,3,1,5),_FrxStartTest_Type())
frxStartTest.setMaxAccess(_D)
if mibBuilder.loadTexts:frxStartTest.setStatus(_A)
class _FrxBertRst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),('resetBert',2)))
_FrxBertRst_Type.__name__=_B
_FrxBertRst_Object=MibTableColumn
frxBertRst=_FrxBertRst_Object((1,3,6,1,4,1,1570,1,6,3,1,6),_FrxBertRst_Type())
frxBertRst.setMaxAccess(_D)
if mibBuilder.loadTexts:frxBertRst.setStatus(_A)
_FrxBertBE_Type=Counter32
_FrxBertBE_Object=MibTableColumn
frxBertBE=_FrxBertBE_Object((1,3,6,1,4,1,1570,1,6,3,1,7),_FrxBertBE_Type())
frxBertBE.setMaxAccess(_C)
if mibBuilder.loadTexts:frxBertBE.setStatus(_A)
_FrxBertTestTime_Type=TimeTicks
_FrxBertTestTime_Object=MibTableColumn
frxBertTestTime=_FrxBertTestTime_Object((1,3,6,1,4,1,1570,1,6,3,1,8),_FrxBertTestTime_Type())
frxBertTestTime.setMaxAccess(_C)
if mibBuilder.loadTexts:frxBertTestTime.setStatus(_A)
class _FrxTestInProg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('testInProgress',1),('normalOperation',2)))
_FrxTestInProg_Type.__name__=_B
_FrxTestInProg_Object=MibTableColumn
frxTestInProg=_FrxTestInProg_Object((1,3,6,1,4,1,1570,1,6,3,1,9),_FrxTestInProg_Type())
frxTestInProg.setMaxAccess(_C)
if mibBuilder.loadTexts:frxTestInProg.setStatus(_A)
_FrxUThrTable_Object=MibTable
frxUThrTable=_FrxUThrTable_Object((1,3,6,1,4,1,1570,1,6,4))
if mibBuilder.loadTexts:frxUThrTable.setStatus(_A)
_FrxUThrEntry_Object=MibTableRow
frxUThrEntry=_FrxUThrEntry_Object((1,3,6,1,4,1,1570,1,6,4,1))
frxUThrEntry.setIndexNames((0,_E,_F),(0,_E,_G),(0,_E,_I),(0,_E,_M))
if mibBuilder.loadTexts:frxUThrEntry.setStatus(_A)
class _FrxPAddrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_U,1),(_V,2),(_W,3),(_X,4),(_Y,5),(_Z,6),(_a,7)))
_FrxPAddrIndex_Type.__name__=_B
_FrxPAddrIndex_Object=MibTableColumn
frxPAddrIndex=_FrxPAddrIndex_Object((1,3,6,1,4,1,1570,1,6,4,1,1),_FrxPAddrIndex_Type())
frxPAddrIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:frxPAddrIndex.setStatus(_A)
class _FrxChEsTh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_FrxChEsTh_Type.__name__=_B
_FrxChEsTh_Object=MibTableColumn
frxChEsTh=_FrxChEsTh_Object((1,3,6,1,4,1,1570,1,6,4,1,2),_FrxChEsTh_Type())
frxChEsTh.setMaxAccess(_D)
if mibBuilder.loadTexts:frxChEsTh.setStatus(_A)
class _FrxCdEsTh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FrxCdEsTh_Type.__name__=_B
_FrxCdEsTh_Object=MibTableColumn
frxCdEsTh=_FrxCdEsTh_Object((1,3,6,1,4,1,1570,1,6,4,1,3),_FrxCdEsTh_Type())
frxCdEsTh.setMaxAccess(_D)
if mibBuilder.loadTexts:frxCdEsTh.setStatus(_A)
class _FrxChSesTh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_FrxChSesTh_Type.__name__=_B
_FrxChSesTh_Object=MibTableColumn
frxChSesTh=_FrxChSesTh_Object((1,3,6,1,4,1,1570,1,6,4,1,4),_FrxChSesTh_Type())
frxChSesTh.setMaxAccess(_D)
if mibBuilder.loadTexts:frxChSesTh.setStatus(_A)
class _FrxCdSesTh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FrxCdSesTh_Type.__name__=_B
_FrxCdSesTh_Object=MibTableColumn
frxCdSesTh=_FrxCdSesTh_Object((1,3,6,1,4,1,1570,1,6,4,1,5),_FrxCdSesTh_Type())
frxCdSesTh.setMaxAccess(_D)
if mibBuilder.loadTexts:frxCdSesTh.setStatus(_A)
class _FrxAlertMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FrxAlertMask_Type.__name__=_B
_FrxAlertMask_Object=MibTableColumn
frxAlertMask=_FrxAlertMask_Object((1,3,6,1,4,1,1570,1,6,4,1,6),_FrxAlertMask_Type())
frxAlertMask.setMaxAccess(_D)
if mibBuilder.loadTexts:frxAlertMask.setStatus(_A)
class _FrxThCond_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FrxThCond_Type.__name__=_B
_FrxThCond_Object=MibTableColumn
frxThCond=_FrxThCond_Object((1,3,6,1,4,1,1570,1,6,4,1,7),_FrxThCond_Type())
frxThCond.setMaxAccess(_D)
if mibBuilder.loadTexts:frxThCond.setStatus(_A)
_FrxUPerfTable_Object=MibTable
frxUPerfTable=_FrxUPerfTable_Object((1,3,6,1,4,1,1570,1,6,5))
if mibBuilder.loadTexts:frxUPerfTable.setStatus(_A)
_FrxUPerfEntry_Object=MibTableRow
frxUPerfEntry=_FrxUPerfEntry_Object((1,3,6,1,4,1,1570,1,6,5,1))
frxUPerfEntry.setIndexNames((0,_E,_F),(0,_E,_G),(0,_E,_I),(0,_E,_M))
if mibBuilder.loadTexts:frxUPerfEntry.setStatus(_A)
class _FrxResetPM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),('resetPM',2)))
_FrxResetPM_Type.__name__=_B
_FrxResetPM_Object=MibTableColumn
frxResetPM=_FrxResetPM_Object((1,3,6,1,4,1,1570,1,6,5,1,1),_FrxResetPM_Type())
frxResetPM.setMaxAccess(_D)
if mibBuilder.loadTexts:frxResetPM.setStatus(_A)
class _FrxPMtype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('segmentedPM',1),('pathPM',2)))
_FrxPMtype_Type.__name__=_B
_FrxPMtype_Object=MibTableColumn
frxPMtype=_FrxPMtype_Object((1,3,6,1,4,1,1570,1,6,5,1,2),_FrxPMtype_Type())
frxPMtype.setMaxAccess(_C)
if mibBuilder.loadTexts:frxPMtype.setStatus(_A)
class _FrxChEsTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_FrxChEsTx_Type.__name__=_B
_FrxChEsTx_Object=MibTableColumn
frxChEsTx=_FrxChEsTx_Object((1,3,6,1,4,1,1570,1,6,5,1,3),_FrxChEsTx_Type())
frxChEsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxChEsTx.setStatus(_A)
class _FrxChEsRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_FrxChEsRx_Type.__name__=_B
_FrxChEsRx_Object=MibTableColumn
frxChEsRx=_FrxChEsRx_Object((1,3,6,1,4,1,1570,1,6,5,1,4),_FrxChEsRx_Type())
frxChEsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxChEsRx.setStatus(_A)
class _FrxPhEsTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_FrxPhEsTx_Type.__name__=_B
_FrxPhEsTx_Object=MibTableColumn
frxPhEsTx=_FrxPhEsTx_Object((1,3,6,1,4,1,1570,1,6,5,1,5),_FrxPhEsTx_Type())
frxPhEsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxPhEsTx.setStatus(_A)
class _FrxPhEsRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_FrxPhEsRx_Type.__name__=_B
_FrxPhEsRx_Object=MibTableColumn
frxPhEsRx=_FrxPhEsRx_Object((1,3,6,1,4,1,1570,1,6,5,1,6),_FrxPhEsRx_Type())
frxPhEsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxPhEsRx.setStatus(_A)
class _FrxH2EsTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_FrxH2EsTx_Type.__name__=_B
_FrxH2EsTx_Object=MibTableColumn
frxH2EsTx=_FrxH2EsTx_Object((1,3,6,1,4,1,1570,1,6,5,1,7),_FrxH2EsTx_Type())
frxH2EsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxH2EsTx.setStatus(_A)
class _FrxH2EsRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_FrxH2EsRx_Type.__name__=_B
_FrxH2EsRx_Object=MibTableColumn
frxH2EsRx=_FrxH2EsRx_Object((1,3,6,1,4,1,1570,1,6,5,1,8),_FrxH2EsRx_Type())
frxH2EsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxH2EsRx.setStatus(_A)
class _FrxH3EsTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_FrxH3EsTx_Type.__name__=_B
_FrxH3EsTx_Object=MibTableColumn
frxH3EsTx=_FrxH3EsTx_Object((1,3,6,1,4,1,1570,1,6,5,1,9),_FrxH3EsTx_Type())
frxH3EsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxH3EsTx.setStatus(_A)
class _FrxH3EsRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_FrxH3EsRx_Type.__name__=_B
_FrxH3EsRx_Object=MibTableColumn
frxH3EsRx=_FrxH3EsRx_Object((1,3,6,1,4,1,1570,1,6,5,1,10),_FrxH3EsRx_Type())
frxH3EsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxH3EsRx.setStatus(_A)
class _FrxH4EsTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_FrxH4EsTx_Type.__name__=_B
_FrxH4EsTx_Object=MibTableColumn
frxH4EsTx=_FrxH4EsTx_Object((1,3,6,1,4,1,1570,1,6,5,1,11),_FrxH4EsTx_Type())
frxH4EsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxH4EsTx.setStatus(_A)
class _FrxH4EsRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_FrxH4EsRx_Type.__name__=_B
_FrxH4EsRx_Object=MibTableColumn
frxH4EsRx=_FrxH4EsRx_Object((1,3,6,1,4,1,1570,1,6,5,1,12),_FrxH4EsRx_Type())
frxH4EsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxH4EsRx.setStatus(_A)
class _FrxH5EsTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_FrxH5EsTx_Type.__name__=_B
_FrxH5EsTx_Object=MibTableColumn
frxH5EsTx=_FrxH5EsTx_Object((1,3,6,1,4,1,1570,1,6,5,1,13),_FrxH5EsTx_Type())
frxH5EsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxH5EsTx.setStatus(_A)
class _FrxH5EsRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_FrxH5EsRx_Type.__name__=_B
_FrxH5EsRx_Object=MibTableColumn
frxH5EsRx=_FrxH5EsRx_Object((1,3,6,1,4,1,1570,1,6,5,1,14),_FrxH5EsRx_Type())
frxH5EsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxH5EsRx.setStatus(_A)
class _FrxH6EsTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_FrxH6EsTx_Type.__name__=_B
_FrxH6EsTx_Object=MibTableColumn
frxH6EsTx=_FrxH6EsTx_Object((1,3,6,1,4,1,1570,1,6,5,1,15),_FrxH6EsTx_Type())
frxH6EsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxH6EsTx.setStatus(_A)
class _FrxH6EsRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_FrxH6EsRx_Type.__name__=_B
_FrxH6EsRx_Object=MibTableColumn
frxH6EsRx=_FrxH6EsRx_Object((1,3,6,1,4,1,1570,1,6,5,1,16),_FrxH6EsRx_Type())
frxH6EsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxH6EsRx.setStatus(_A)
class _FrxH7EsTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_FrxH7EsTx_Type.__name__=_B
_FrxH7EsTx_Object=MibTableColumn
frxH7EsTx=_FrxH7EsTx_Object((1,3,6,1,4,1,1570,1,6,5,1,17),_FrxH7EsTx_Type())
frxH7EsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxH7EsTx.setStatus(_A)
class _FrxH7EsRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_FrxH7EsRx_Type.__name__=_B
_FrxH7EsRx_Object=MibTableColumn
frxH7EsRx=_FrxH7EsRx_Object((1,3,6,1,4,1,1570,1,6,5,1,18),_FrxH7EsRx_Type())
frxH7EsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxH7EsRx.setStatus(_A)
class _FrxH8EsTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_FrxH8EsTx_Type.__name__=_B
_FrxH8EsTx_Object=MibTableColumn
frxH8EsTx=_FrxH8EsTx_Object((1,3,6,1,4,1,1570,1,6,5,1,19),_FrxH8EsTx_Type())
frxH8EsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxH8EsTx.setStatus(_A)
class _FrxH8EsRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_FrxH8EsRx_Type.__name__=_B
_FrxH8EsRx_Object=MibTableColumn
frxH8EsRx=_FrxH8EsRx_Object((1,3,6,1,4,1,1570,1,6,5,1,20),_FrxH8EsRx_Type())
frxH8EsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxH8EsRx.setStatus(_A)
class _FrxCdEsTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FrxCdEsTx_Type.__name__=_B
_FrxCdEsTx_Object=MibTableColumn
frxCdEsTx=_FrxCdEsTx_Object((1,3,6,1,4,1,1570,1,6,5,1,21),_FrxCdEsTx_Type())
frxCdEsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxCdEsTx.setStatus(_A)
class _FrxCdEsRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FrxCdEsRx_Type.__name__=_B
_FrxCdEsRx_Object=MibTableColumn
frxCdEsRx=_FrxCdEsRx_Object((1,3,6,1,4,1,1570,1,6,5,1,22),_FrxCdEsRx_Type())
frxCdEsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxCdEsRx.setStatus(_A)
class _FrxPdEsTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FrxPdEsTx_Type.__name__=_B
_FrxPdEsTx_Object=MibTableColumn
frxPdEsTx=_FrxPdEsTx_Object((1,3,6,1,4,1,1570,1,6,5,1,23),_FrxPdEsTx_Type())
frxPdEsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxPdEsTx.setStatus(_A)
class _FrxPdEsRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FrxPdEsRx_Type.__name__=_B
_FrxPdEsRx_Object=MibTableColumn
frxPdEsRx=_FrxPdEsRx_Object((1,3,6,1,4,1,1570,1,6,5,1,24),_FrxPdEsRx_Type())
frxPdEsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxPdEsRx.setStatus(_A)
class _FrxChSesTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_FrxChSesTx_Type.__name__=_B
_FrxChSesTx_Object=MibTableColumn
frxChSesTx=_FrxChSesTx_Object((1,3,6,1,4,1,1570,1,6,5,1,25),_FrxChSesTx_Type())
frxChSesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxChSesTx.setStatus(_A)
class _FrxChSesRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_FrxChSesRx_Type.__name__=_B
_FrxChSesRx_Object=MibTableColumn
frxChSesRx=_FrxChSesRx_Object((1,3,6,1,4,1,1570,1,6,5,1,26),_FrxChSesRx_Type())
frxChSesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxChSesRx.setStatus(_A)
class _FrxPhSesTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_FrxPhSesTx_Type.__name__=_B
_FrxPhSesTx_Object=MibTableColumn
frxPhSesTx=_FrxPhSesTx_Object((1,3,6,1,4,1,1570,1,6,5,1,27),_FrxPhSesTx_Type())
frxPhSesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxPhSesTx.setStatus(_A)
class _FrxPhSesRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_FrxPhSesRx_Type.__name__=_B
_FrxPhSesRx_Object=MibTableColumn
frxPhSesRx=_FrxPhSesRx_Object((1,3,6,1,4,1,1570,1,6,5,1,28),_FrxPhSesRx_Type())
frxPhSesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxPhSesRx.setStatus(_A)
class _FrxCdSesTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FrxCdSesTx_Type.__name__=_B
_FrxCdSesTx_Object=MibTableColumn
frxCdSesTx=_FrxCdSesTx_Object((1,3,6,1,4,1,1570,1,6,5,1,29),_FrxCdSesTx_Type())
frxCdSesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxCdSesTx.setStatus(_A)
class _FrxCdSesRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FrxCdSesRx_Type.__name__=_B
_FrxCdSesRx_Object=MibTableColumn
frxCdSesRx=_FrxCdSesRx_Object((1,3,6,1,4,1,1570,1,6,5,1,30),_FrxCdSesRx_Type())
frxCdSesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxCdSesRx.setStatus(_A)
class _FrxPdSesTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FrxPdSesTx_Type.__name__=_B
_FrxPdSesTx_Object=MibTableColumn
frxPdSesTx=_FrxPdSesTx_Object((1,3,6,1,4,1,1570,1,6,5,1,31),_FrxPdSesTx_Type())
frxPdSesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxPdSesTx.setStatus(_A)
class _FrxPdSesRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FrxPdSesRx_Type.__name__=_B
_FrxPdSesRx_Object=MibTableColumn
frxPdSesRx=_FrxPdSesRx_Object((1,3,6,1,4,1,1570,1,6,5,1,32),_FrxPdSesRx_Type())
frxPdSesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxPdSesRx.setStatus(_A)
class _FrxChBeTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FrxChBeTx_Type.__name__=_B
_FrxChBeTx_Object=MibTableColumn
frxChBeTx=_FrxChBeTx_Object((1,3,6,1,4,1,1570,1,6,5,1,33),_FrxChBeTx_Type())
frxChBeTx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxChBeTx.setStatus(_A)
class _FrxChBeRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FrxChBeRx_Type.__name__=_B
_FrxChBeRx_Object=MibTableColumn
frxChBeRx=_FrxChBeRx_Object((1,3,6,1,4,1,1570,1,6,5,1,34),_FrxChBeRx_Type())
frxChBeRx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxChBeRx.setStatus(_A)
class _FrxPhBeTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FrxPhBeTx_Type.__name__=_B
_FrxPhBeTx_Object=MibTableColumn
frxPhBeTx=_FrxPhBeTx_Object((1,3,6,1,4,1,1570,1,6,5,1,35),_FrxPhBeTx_Type())
frxPhBeTx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxPhBeTx.setStatus(_A)
class _FrxPhBeRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FrxPhBeRx_Type.__name__=_B
_FrxPhBeRx_Object=MibTableColumn
frxPhBeRx=_FrxPhBeRx_Object((1,3,6,1,4,1,1570,1,6,5,1,36),_FrxPhBeRx_Type())
frxPhBeRx.setMaxAccess(_C)
if mibBuilder.loadTexts:frxPhBeRx.setStatus(_A)
frxDownloadTrap=NotificationType((1,3,6,1,4,1,1570,1,0,1))
frxDownloadTrap.setObjects(*((_E,_F),(_E,_G)))
if mibBuilder.loadTexts:frxDownloadTrap.setStatus('')
frxUPerfTrap=NotificationType((1,3,6,1,4,1,1570,1,0,2))
frxUPerfTrap.setObjects(*((_E,_F),(_E,_G)))
if mibBuilder.loadTexts:frxUPerfTrap.setStatus('')
frxInsertChUTrap=NotificationType((1,3,6,1,4,1,1570,1,0,3))
frxInsertChUTrap.setObjects(*((_E,_F),(_E,_G)))
if mibBuilder.loadTexts:frxInsertChUTrap.setStatus('')
frxRemoveChUTrap=NotificationType((1,3,6,1,4,1,1570,1,0,4))
frxRemoveChUTrap.setObjects(*((_E,_F),(_E,_G)))
if mibBuilder.loadTexts:frxRemoveChUTrap.setStatus('')
frxDConfigFailed=NotificationType((1,3,6,1,4,1,1570,1,0,5))
frxDConfigFailed.setObjects(*((_E,_F),(_E,_G)))
if mibBuilder.loadTexts:frxDConfigFailed.setStatus('')
mibBuilder.exportSymbols(_E,**{_H:DisplayString,'ciscoTelesend':ciscoTelesend,'frMux':frMux,'frxDownloadTrap':frxDownloadTrap,'frxUPerfTrap':frxUPerfTrap,'frxInsertChUTrap':frxInsertChUTrap,'frxRemoveChUTrap':frxRemoveChUTrap,'frxDConfigFailed':frxDConfigFailed,'frxSys':frxSys,'frxSysDescr':frxSysDescr,'frxClockHour':frxClockHour,'frxClockMin':frxClockMin,'frxClockSec':frxClockSec,'frxUpTime':frxUpTime,'frxAdminContact':frxAdminContact,'frxSysName':frxSysName,'frxSysLoc':frxSysLoc,'frxSysVersion':frxSysVersion,'frxUPerfTrapEnable':frxUPerfTrapEnable,'frxAgtLinkErrors':frxAgtLinkErrors,'frxAgtProtErrors':frxAgtProtErrors,'frxAgtChInactive':frxAgtChInactive,'frxAgtChStatus':frxAgtChStatus,'frxDefault':frxDefault,'frxDefaultEnable':frxDefaultEnable,'frxDefaultTrap':frxDefaultTrap,'frxDConfigSrc':frxDConfigSrc,'frxDMgtT391':frxDMgtT391,'frxDMgtT392':frxDMgtT392,'frxDMgtN391':frxDMgtN391,'frxDMgtN392':frxDMgtN392,'frxDMgtN393':frxDMgtN393,'frxDPortSpeed':frxDPortSpeed,'frxDPortProtocol':frxDPortProtocol,'frxDCktCIR':frxDCktCIR,'frxDCktBc':frxDCktBc,'frxDCktBe':frxDCktBe,'frxBank':frxBank,'frxBankTable':frxBankTable,'frxBankEntry':frxBankEntry,_F:frxBankIndex,'frxBankType':frxBankType,'frxChUnit':frxChUnit,'frxChUTable':frxChUTable,'frxChUEntry':frxChUEntry,_G:frxChUIndex,'frxChUType':frxChUType,'frxChUVersion':frxChUVersion,'frxSigProtocol':frxSigProtocol,'frxConfigSrc':frxConfigSrc,'frxDLCIAdLen':frxDLCIAdLen,'frxNetInOctets':frxNetInOctets,'frxNetOutOctets':frxNetOutOctets,'frxNetBadFrames':frxNetBadFrames,'frxNetHDLCEs':frxNetHDLCEs,'frxNetCRCEs':frxNetCRCEs,'frxNetLinkEs':frxNetLinkEs,'frxNetFrShEs':frxNetFrShEs,'frxNetFrLgEs':frxNetFrLgEs,'frxNetPPPEs':frxNetPPPEs,'frxNetBufEs':frxNetBufEs,'frxMgt':frxMgt,'frxMgtTable':frxMgtTable,'frxMgtEntry':frxMgtEntry,'frxPortsInSvc':frxPortsInSvc,'frxMgtT391':frxMgtT391,'frxMgtT392':frxMgtT392,'frxMgtN391':frxMgtN391,'frxMgtN392':frxMgtN392,'frxMgtN393':frxMgtN393,'frxNetLinkErrors':frxNetLinkErrors,'frxNetProtErrors':frxNetProtErrors,'frxNetChInactive':frxNetChInactive,'frxNetChStatus':frxNetChStatus,'frxMgtPortTable':frxMgtPortTable,'frxMgtPortEntry':frxMgtPortEntry,_I:frxPortIndex,'frxPortLinkErrors':frxPortLinkErrors,'frxPortProtErrors':frxPortProtErrors,'frxPortChInactive':frxPortChInactive,'frxPort':frxPort,'frxPortTable':frxPortTable,'frxPortEntry':frxPortEntry,'frxPortSpeed':frxPortSpeed,'frxPortProtocol':frxPortProtocol,'frxDSLStatus':frxDSLStatus,'frxPVCAssigned':frxPVCAssigned,'frxLastChange':frxLastChange,'frxBrite':frxBrite,'frxDSLInOctets':frxDSLInOctets,'frxDSLOutOctets':frxDSLOutOctets,'frxT1InOctets':frxT1InOctets,'frxT1OutOctets':frxT1OutOctets,'frxDSLBadFrames':frxDSLBadFrames,'frxDSLHDLCEs':frxDSLHDLCEs,'frxDSLCRCEs':frxDSLCRCEs,'frxDSLLinkEs':frxDSLLinkEs,'frxDSLFrShEs':frxDSLFrShEs,'frxDSLFrLgEs':frxDSLFrLgEs,'frxDSLDLCIEs':frxDSLDLCIEs,'frxTxBuf':frxTxBuf,'frxRxBuf':frxRxBuf,'frxPortNetEs':frxPortNetEs,'frxCircuitTable':frxCircuitTable,'frxCircuitEntry':frxCircuitEntry,_T:frxPvcIndex,'frxCktCIR':frxCktCIR,'frxCktBc':frxCktBc,'frxCktBe':frxCktBe,'frxFarEndOpStat':frxFarEndOpStat,'frxCktInOctets':frxCktInOctets,'frxCktOutOctets':frxCktOutOctets,'frxCktInFrames':frxCktInFrames,'frxCktOutFrames':frxCktOutFrames,'frxCktDiscards':frxCktDiscards,'frxUEocTable':frxUEocTable,'frxUEocEntry':frxUEocEntry,'frxTestPort':frxTestPort,'frxTestType':frxTestType,'frxLoopLoc':frxLoopLoc,'frxLoopCh':frxLoopCh,'frxStartTest':frxStartTest,'frxBertRst':frxBertRst,'frxBertBE':frxBertBE,'frxBertTestTime':frxBertTestTime,'frxTestInProg':frxTestInProg,'frxUThrTable':frxUThrTable,'frxUThrEntry':frxUThrEntry,_M:frxPAddrIndex,'frxChEsTh':frxChEsTh,'frxCdEsTh':frxCdEsTh,'frxChSesTh':frxChSesTh,'frxCdSesTh':frxCdSesTh,'frxAlertMask':frxAlertMask,'frxThCond':frxThCond,'frxUPerfTable':frxUPerfTable,'frxUPerfEntry':frxUPerfEntry,'frxResetPM':frxResetPM,'frxPMtype':frxPMtype,'frxChEsTx':frxChEsTx,'frxChEsRx':frxChEsRx,'frxPhEsTx':frxPhEsTx,'frxPhEsRx':frxPhEsRx,'frxH2EsTx':frxH2EsTx,'frxH2EsRx':frxH2EsRx,'frxH3EsTx':frxH3EsTx,'frxH3EsRx':frxH3EsRx,'frxH4EsTx':frxH4EsTx,'frxH4EsRx':frxH4EsRx,'frxH5EsTx':frxH5EsTx,'frxH5EsRx':frxH5EsRx,'frxH6EsTx':frxH6EsTx,'frxH6EsRx':frxH6EsRx,'frxH7EsTx':frxH7EsTx,'frxH7EsRx':frxH7EsRx,'frxH8EsTx':frxH8EsTx,'frxH8EsRx':frxH8EsRx,'frxCdEsTx':frxCdEsTx,'frxCdEsRx':frxCdEsRx,'frxPdEsTx':frxPdEsTx,'frxPdEsRx':frxPdEsRx,'frxChSesTx':frxChSesTx,'frxChSesRx':frxChSesRx,'frxPhSesTx':frxPhSesTx,'frxPhSesRx':frxPhSesRx,'frxCdSesTx':frxCdSesTx,'frxCdSesRx':frxCdSesRx,'frxPdSesTx':frxPdSesTx,'frxPdSesRx':frxPdSesRx,'frxChBeTx':frxChBeTx,'frxChBeRx':frxChBeRx,'frxPhBeTx':frxPhBeTx,'frxPhBeRx':frxPhBeRx})