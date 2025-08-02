_i='itsSnkTtpLocalDsti'
_h='itsSnkTtpIndex'
_g='itsSrcTtpLocalDsti'
_f='itsSrcTtpIndex'
_e='ItsProtectionStatus'
_d='itsIfSdiAncIndex'
_c='itsIfSdiVbiIndex'
_b='itsIfSdiAudioIndex'
_a='obsolete'
_Z='disable'
_Y='enable'
_X='unknown'
_W='compatible'
_V='multicast'
_U='warning'
_T='Gauge32'
_S='read-create'
_R='notApplicable'
_Q='dormant'
_P='no'
_O='SnmpAdminString'
_N='down'
_M='up'
_L='none'
_K='notSupported'
_J='Bits'
_I='not-accessible'
_H='TruthValue'
_G='Unsigned32'
_F='itsIfIndex'
_E='NETI-ITS-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Dsti,=mibBuilder.importSymbols('NETI-CHMGR-MIB','Dsti')
netiExperimentalGeneric,=mibBuilder.importSymbols('NETI-COMMON-MIB','netiExperimentalGeneric')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_O)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_J,'Counter32','Counter64',_T,_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowPointer,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','RowStatus','TextualConvention','TimeStamp',_H)
netiItsMIB=ModuleIdentity((1,3,6,1,4,1,2928,6,2,16))
if mibBuilder.loadTexts:netiItsMIB.setRevisions(('2014-09-11 13:00','2014-02-21 15:00','2013-09-30 07:00','2012-12-03 11:00','2012-09-04 14:00','2012-01-20 16:00','2011-12-01 09:00','2011-10-10 13:00','2011-04-27 09:00','2011-04-27 08:00','2011-02-04 12:00','2011-02-03 09:00','2010-08-19 09:00','2010-01-19 09:00','2009-01-22 15:00','2008-04-17 10:30','2008-01-18 15:00','2007-12-04 16:00','2007-06-29 14:00'))
class ItsTtpIndexList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(8,8))
class ItsProtectionStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unavailable',1),('unprotected',2),('standbyProtected',3),('hitlessCapable',4),('hitlessProtected',5)))
_ItsObjects_ObjectIdentity=ObjectIdentity
itsObjects=_ItsObjects_ObjectIdentity((1,3,6,1,4,1,2928,6,2,16,1))
_ItsIfGroup_ObjectIdentity=ObjectIdentity
itsIfGroup=_ItsIfGroup_ObjectIdentity((1,3,6,1,4,1,2928,6,2,16,1,1))
_ItsIfLastChange_Type=TimeStamp
_ItsIfLastChange_Object=MibScalar
itsIfLastChange=_ItsIfLastChange_Object((1,3,6,1,4,1,2928,6,2,16,1,1,1),_ItsIfLastChange_Type())
itsIfLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfLastChange.setStatus(_A)
_ItsIfTable_Object=MibTable
itsIfTable=_ItsIfTable_Object((1,3,6,1,4,1,2928,6,2,16,1,1,2))
if mibBuilder.loadTexts:itsIfTable.setStatus(_A)
_ItsIfEntry_Object=MibTableRow
itsIfEntry=_ItsIfEntry_Object((1,3,6,1,4,1,2928,6,2,16,1,1,2,1))
itsIfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:itsIfEntry.setStatus(_A)
_ItsIfIndex_Type=Unsigned32
_ItsIfIndex_Object=MibTableColumn
itsIfIndex=_ItsIfIndex_Object((1,3,6,1,4,1,2928,6,2,16,1,1,2,1,1),_ItsIfIndex_Type())
itsIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:itsIfIndex.setStatus(_A)
_ItsIfIfIndex_Type=Integer32
_ItsIfIfIndex_Object=MibTableColumn
itsIfIfIndex=_ItsIfIfIndex_Object((1,3,6,1,4,1,2928,6,2,16,1,1,2,1,2),_ItsIfIfIndex_Type())
itsIfIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfIfIndex.setStatus(_A)
_ItsIfName_Type=SnmpAdminString
_ItsIfName_Object=MibTableColumn
itsIfName=_ItsIfName_Object((1,3,6,1,4,1,2928,6,2,16,1,1,2,1,3),_ItsIfName_Type())
itsIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfName.setStatus(_A)
_ItsIfDescr_Type=SnmpAdminString
_ItsIfDescr_Object=MibTableColumn
itsIfDescr=_ItsIfDescr_Object((1,3,6,1,4,1,2928,6,2,16,1,1,2,1,4),_ItsIfDescr_Type())
itsIfDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfDescr.setStatus(_A)
_ItsIfSpeed_Type=Gauge32
_ItsIfSpeed_Object=MibTableColumn
itsIfSpeed=_ItsIfSpeed_Object((1,3,6,1,4,1,2928,6,2,16,1,1,2,1,5),_ItsIfSpeed_Type())
itsIfSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfSpeed.setStatus(_A)
class _ItsIfSuppressAlarm_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_K,0),(_L,1),(_U,2),('all',3)))
_ItsIfSuppressAlarm_Type.__name__=_D
_ItsIfSuppressAlarm_Object=MibTableColumn
itsIfSuppressAlarm=_ItsIfSuppressAlarm_Object((1,3,6,1,4,1,2928,6,2,16,1,1,2,1,6),_ItsIfSuppressAlarm_Type())
itsIfSuppressAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfSuppressAlarm.setStatus(_A)
class _ItsIfLoopMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_K,0),(_L,1),('line',2),('dtm',3)))
_ItsIfLoopMode_Type.__name__=_D
_ItsIfLoopMode_Object=MibTableColumn
itsIfLoopMode=_ItsIfLoopMode_Object((1,3,6,1,4,1,2928,6,2,16,1,1,2,1,7),_ItsIfLoopMode_Type())
itsIfLoopMode.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfLoopMode.setStatus(_A)
class _ItsIfLoopTime_Type(Gauge32):defaultValue=0;subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ItsIfLoopTime_Type.__name__=_T
_ItsIfLoopTime_Object=MibTableColumn
itsIfLoopTime=_ItsIfLoopTime_Object((1,3,6,1,4,1,2928,6,2,16,1,1,2,1,8),_ItsIfLoopTime_Type())
itsIfLoopTime.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfLoopTime.setStatus('deprecated')
class _ItsIfCapabilities_Type(Bits):namedValues=NamedValues(*((_V,0),('allowProtection',1),('requireCapacity',2),('channelPM',3),('interfacePM',4),('ttp',5),('mon',6),('loopl',7),('loopd',8),('sdi1483',9),('sdi1485',10),('sdi288',11),('sdi270',12),('sdi2967',13),('sdi2970',14),('fs',15),('avrs',16),('madi',19),('ref',20),('j2kEnc',21),('j2kDec',22),('hitps',23),('psType3',24),('dvrs',25),(_W,31)))
_ItsIfCapabilities_Type.__name__=_J
_ItsIfCapabilities_Object=MibTableColumn
itsIfCapabilities=_ItsIfCapabilities_Object((1,3,6,1,4,1,2928,6,2,16,1,1,2,1,9),_ItsIfCapabilities_Type())
itsIfCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfCapabilities.setStatus(_A)
class _ItsIfProperties_Type(Bits):namedValues=NamedValues(('tbd',0))
_ItsIfProperties_Type.__name__=_J
_ItsIfProperties_Object=MibTableColumn
itsIfProperties=_ItsIfProperties_Object((1,3,6,1,4,1,2928,6,2,16,1,1,2,1,10),_ItsIfProperties_Type())
itsIfProperties.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfProperties.setStatus(_A)
class _ItsIfDefects_Type(Bits):namedValues=NamedValues(*(('los',0),('lof',1),('ais',2),('lop',3),('lod',4),('rdi',5),('lol',6)))
_ItsIfDefects_Type.__name__=_J
_ItsIfDefects_Object=MibTableColumn
itsIfDefects=_ItsIfDefects_Object((1,3,6,1,4,1,2928,6,2,16,1,1,2,1,11),_ItsIfDefects_Type())
itsIfDefects.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfDefects.setStatus(_A)
_ItsIfFailure_Type=SnmpAdminString
_ItsIfFailure_Object=MibTableColumn
itsIfFailure=_ItsIfFailure_Object((1,3,6,1,4,1,2928,6,2,16,1,1,2,1,12),_ItsIfFailure_Type())
itsIfFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfFailure.setStatus(_A)
_ItsIfPMReference_Type=RowPointer
_ItsIfPMReference_Object=MibTableColumn
itsIfPMReference=_ItsIfPMReference_Object((1,3,6,1,4,1,2928,6,2,16,1,1,2,1,13),_ItsIfPMReference_Type())
itsIfPMReference.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfPMReference.setStatus(_A)
class _ItsIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5,6)));namedValues=NamedValues(*((_M,1),(_N,2),(_X,4),(_Q,5),('notPresent',6)))
_ItsIfOperStatus_Type.__name__=_D
_ItsIfOperStatus_Object=MibTableColumn
itsIfOperStatus=_ItsIfOperStatus_Object((1,3,6,1,4,1,2928,6,2,16,1,1,2,1,14),_ItsIfOperStatus_Type())
itsIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfOperStatus.setStatus(_A)
class _ItsIfTxMuteOnFault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_K,0),(_Y,1),(_Z,2),('freeze',3)))
_ItsIfTxMuteOnFault_Type.__name__=_D
_ItsIfTxMuteOnFault_Object=MibTableColumn
itsIfTxMuteOnFault=_ItsIfTxMuteOnFault_Object((1,3,6,1,4,1,2928,6,2,16,1,1,2,1,15),_ItsIfTxMuteOnFault_Type())
itsIfTxMuteOnFault.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfTxMuteOnFault.setStatus(_A)
class _ItsIfPurpose_Type(SnmpAdminString):defaultHexValue=''
_ItsIfPurpose_Type.__name__=_O
_ItsIfPurpose_Object=MibTableColumn
itsIfPurpose=_ItsIfPurpose_Object((1,3,6,1,4,1,2928,6,2,16,1,1,2,1,16),_ItsIfPurpose_Type())
itsIfPurpose.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfPurpose.setStatus(_A)
class _ItsIfInterfaceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('pdh',1),('sdh',2),('sdi',3),('dvb',4),('aes',5),('mon',6)))
_ItsIfInterfaceType_Type.__name__=_D
_ItsIfInterfaceType_Object=MibTableColumn
itsIfInterfaceType=_ItsIfInterfaceType_Object((1,3,6,1,4,1,2928,6,2,16,1,1,2,1,17),_ItsIfInterfaceType_Type())
itsIfInterfaceType.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfInterfaceType.setStatus(_A)
_ItsIfMembersSrc_Type=ItsTtpIndexList
_ItsIfMembersSrc_Object=MibTableColumn
itsIfMembersSrc=_ItsIfMembersSrc_Object((1,3,6,1,4,1,2928,6,2,16,1,1,2,1,18),_ItsIfMembersSrc_Type())
itsIfMembersSrc.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfMembersSrc.setStatus(_A)
_ItsIfMembersSnk_Type=ItsTtpIndexList
_ItsIfMembersSnk_Object=MibTableColumn
itsIfMembersSnk=_ItsIfMembersSnk_Object((1,3,6,1,4,1,2928,6,2,16,1,1,2,1,19),_ItsIfMembersSnk_Type())
itsIfMembersSnk.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfMembersSnk.setStatus(_A)
_ItsIfPdhTable_Object=MibTable
itsIfPdhTable=_ItsIfPdhTable_Object((1,3,6,1,4,1,2928,6,2,16,1,1,3))
if mibBuilder.loadTexts:itsIfPdhTable.setStatus(_A)
_ItsIfPdhEntry_Object=MibTableRow
itsIfPdhEntry=_ItsIfPdhEntry_Object((1,3,6,1,4,1,2928,6,2,16,1,1,3,1))
itsIfPdhEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:itsIfPdhEntry.setStatus(_A)
class _ItsIfPdhSignal_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('e3',1),('ds3',2)))
_ItsIfPdhSignal_Type.__name__=_D
_ItsIfPdhSignal_Object=MibTableColumn
itsIfPdhSignal=_ItsIfPdhSignal_Object((1,3,6,1,4,1,2928,6,2,16,1,1,3,1,1),_ItsIfPdhSignal_Type())
itsIfPdhSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfPdhSignal.setStatus(_A)
class _ItsIfPdhFraming_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_L,1),('g751',2),('g832',3),('cbit',4),('m13',5)))
_ItsIfPdhFraming_Type.__name__=_D
_ItsIfPdhFraming_Object=MibTableColumn
itsIfPdhFraming=_ItsIfPdhFraming_Object((1,3,6,1,4,1,2928,6,2,16,1,1,3,1,2),_ItsIfPdhFraming_Type())
itsIfPdhFraming.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfPdhFraming.setStatus(_A)
_ItsIfSdhTable_Object=MibTable
itsIfSdhTable=_ItsIfSdhTable_Object((1,3,6,1,4,1,2928,6,2,16,1,1,4))
if mibBuilder.loadTexts:itsIfSdhTable.setStatus(_A)
_ItsIfSdhEntry_Object=MibTableRow
itsIfSdhEntry=_ItsIfSdhEntry_Object((1,3,6,1,4,1,2928,6,2,16,1,1,4,1))
itsIfSdhEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:itsIfSdhEntry.setStatus(_A)
class _ItsIfSdhTiming_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('loop',1),('internal',2)))
_ItsIfSdhTiming_Type.__name__=_D
_ItsIfSdhTiming_Object=MibTableColumn
itsIfSdhTiming=_ItsIfSdhTiming_Object((1,3,6,1,4,1,2928,6,2,16,1,1,4,1,1),_ItsIfSdhTiming_Type())
itsIfSdhTiming.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfSdhTiming.setStatus(_A)
class _ItsIfSdhMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sdh',1),('sonet',2)))
_ItsIfSdhMode_Type.__name__=_D
_ItsIfSdhMode_Object=MibTableColumn
itsIfSdhMode=_ItsIfSdhMode_Object((1,3,6,1,4,1,2928,6,2,16,1,1,4,1,2),_ItsIfSdhMode_Type())
itsIfSdhMode.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfSdhMode.setStatus(_A)
class _ItsIfSdhSs_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_ItsIfSdhSs_Type.__name__=_G
_ItsIfSdhSs_Object=MibTableColumn
itsIfSdhSs=_ItsIfSdhSs_Object((1,3,6,1,4,1,2928,6,2,16,1,1,4,1,3),_ItsIfSdhSs_Type())
itsIfSdhSs.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfSdhSs.setStatus(_A)
class _ItsIfSdhS1_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_ItsIfSdhS1_Type.__name__=_G
_ItsIfSdhS1_Object=MibTableColumn
itsIfSdhS1=_ItsIfSdhS1_Object((1,3,6,1,4,1,2928,6,2,16,1,1,4,1,4),_ItsIfSdhS1_Type())
itsIfSdhS1.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfSdhS1.setStatus(_A)
_ItsIfSdhSoh_Type=SnmpAdminString
_ItsIfSdhSoh_Object=MibTableColumn
itsIfSdhSoh=_ItsIfSdhSoh_Object((1,3,6,1,4,1,2928,6,2,16,1,1,4,1,5),_ItsIfSdhSoh_Type())
itsIfSdhSoh.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfSdhSoh.setStatus(_A)
_ItsIfSdhPoh_Type=SnmpAdminString
_ItsIfSdhPoh_Object=MibTableColumn
itsIfSdhPoh=_ItsIfSdhPoh_Object((1,3,6,1,4,1,2928,6,2,16,1,1,4,1,6),_ItsIfSdhPoh_Type())
itsIfSdhPoh.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfSdhPoh.setStatus(_A)
_ItsIfSdhJc_Type=SnmpAdminString
_ItsIfSdhJc_Object=MibTableColumn
itsIfSdhJc=_ItsIfSdhJc_Object((1,3,6,1,4,1,2928,6,2,16,1,1,4,1,7),_ItsIfSdhJc_Type())
itsIfSdhJc.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfSdhJc.setStatus(_A)
_ItsIfDvbTable_Object=MibTable
itsIfDvbTable=_ItsIfDvbTable_Object((1,3,6,1,4,1,2928,6,2,16,1,1,5))
if mibBuilder.loadTexts:itsIfDvbTable.setStatus(_A)
_ItsIfDvbEntry_Object=MibTableRow
itsIfDvbEntry=_ItsIfDvbEntry_Object((1,3,6,1,4,1,2928,6,2,16,1,1,5,1))
itsIfDvbEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:itsIfDvbEntry.setStatus(_A)
_ItsIfDvbFormat_Type=SnmpAdminString
_ItsIfDvbFormat_Object=MibTableColumn
itsIfDvbFormat=_ItsIfDvbFormat_Object((1,3,6,1,4,1,2928,6,2,16,1,1,5,1,1),_ItsIfDvbFormat_Type())
itsIfDvbFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfDvbFormat.setStatus(_A)
class _ItsIfDvbOutputMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto',1),('burst',2),('spread',3)))
_ItsIfDvbOutputMode_Type.__name__=_D
_ItsIfDvbOutputMode_Object=MibTableColumn
itsIfDvbOutputMode=_ItsIfDvbOutputMode_Object((1,3,6,1,4,1,2928,6,2,16,1,1,5,1,2),_ItsIfDvbOutputMode_Type())
itsIfDvbOutputMode.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfDvbOutputMode.setStatus(_A)
_ItsIfAesTable_Object=MibTable
itsIfAesTable=_ItsIfAesTable_Object((1,3,6,1,4,1,2928,6,2,16,1,1,6))
if mibBuilder.loadTexts:itsIfAesTable.setStatus(_A)
_ItsIfAesEntry_Object=MibTableRow
itsIfAesEntry=_ItsIfAesEntry_Object((1,3,6,1,4,1,2928,6,2,16,1,1,6,1))
itsIfAesEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:itsIfAesEntry.setStatus(_A)
class _ItsIfAesIsTimingProvider_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),('wordClock',1)))
_ItsIfAesIsTimingProvider_Type.__name__=_D
_ItsIfAesIsTimingProvider_Object=MibTableColumn
itsIfAesIsTimingProvider=_ItsIfAesIsTimingProvider_Object((1,3,6,1,4,1,2928,6,2,16,1,1,6,1,1),_ItsIfAesIsTimingProvider_Type())
itsIfAesIsTimingProvider.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfAesIsTimingProvider.setStatus(_A)
_ItsIfAesReference_Type=Integer32
_ItsIfAesReference_Object=MibTableColumn
itsIfAesReference=_ItsIfAesReference_Object((1,3,6,1,4,1,2928,6,2,16,1,1,6,1,2),_ItsIfAesReference_Type())
itsIfAesReference.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfAesReference.setStatus(_A)
_ItsIfSdiTable_Object=MibTable
itsIfSdiTable=_ItsIfSdiTable_Object((1,3,6,1,4,1,2928,6,2,16,1,1,7))
if mibBuilder.loadTexts:itsIfSdiTable.setStatus(_A)
_ItsIfSdiEntry_Object=MibTableRow
itsIfSdiEntry=_ItsIfSdiEntry_Object((1,3,6,1,4,1,2928,6,2,16,1,1,7,1))
itsIfSdiEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:itsIfSdiEntry.setStatus(_A)
_ItsIfSdiFormat_Type=SnmpAdminString
_ItsIfSdiFormat_Object=MibTableColumn
itsIfSdiFormat=_ItsIfSdiFormat_Object((1,3,6,1,4,1,2928,6,2,16,1,1,7,1,1),_ItsIfSdiFormat_Type())
itsIfSdiFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfSdiFormat.setStatus(_A)
class _ItsIfSdiAutoSense_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_K,0),(_Y,1),(_Z,2)))
_ItsIfSdiAutoSense_Type.__name__=_D
_ItsIfSdiAutoSense_Object=MibTableColumn
itsIfSdiAutoSense=_ItsIfSdiAutoSense_Object((1,3,6,1,4,1,2928,6,2,16,1,1,7,1,2),_ItsIfSdiAutoSense_Type())
itsIfSdiAutoSense.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfSdiAutoSense.setStatus(_A)
class _ItsIfSdiIsTimingProvider_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_P,0),('analog',1),('digital',2)))
_ItsIfSdiIsTimingProvider_Type.__name__=_D
_ItsIfSdiIsTimingProvider_Object=MibTableColumn
itsIfSdiIsTimingProvider=_ItsIfSdiIsTimingProvider_Object((1,3,6,1,4,1,2928,6,2,16,1,1,7,1,3),_ItsIfSdiIsTimingProvider_Type())
itsIfSdiIsTimingProvider.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfSdiIsTimingProvider.setStatus(_A)
_ItsIfSdiReference_Type=Integer32
_ItsIfSdiReference_Object=MibTableColumn
itsIfSdiReference=_ItsIfSdiReference_Object((1,3,6,1,4,1,2928,6,2,16,1,1,7,1,4),_ItsIfSdiReference_Type())
itsIfSdiReference.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfSdiReference.setStatus(_A)
class _ItsIfSdiFsVDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-3,1124))
_ItsIfSdiFsVDelay_Type.__name__=_D
_ItsIfSdiFsVDelay_Object=MibTableColumn
itsIfSdiFsVDelay=_ItsIfSdiFsVDelay_Object((1,3,6,1,4,1,2928,6,2,16,1,1,7,1,5),_ItsIfSdiFsVDelay_Type())
itsIfSdiFsVDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfSdiFsVDelay.setStatus(_a)
class _ItsIfSdiFsHDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-3865,259))
_ItsIfSdiFsHDelay_Type.__name__=_D
_ItsIfSdiFsHDelay_Object=MibTableColumn
itsIfSdiFsHDelay=_ItsIfSdiFsHDelay_Object((1,3,6,1,4,1,2928,6,2,16,1,1,7,1,6),_ItsIfSdiFsHDelay_Type())
itsIfSdiFsHDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfSdiFsHDelay.setStatus(_a)
class _ItsIfSdiFsDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-20854167,20854167))
_ItsIfSdiFsDelay_Type.__name__=_D
_ItsIfSdiFsDelay_Object=MibTableColumn
itsIfSdiFsDelay=_ItsIfSdiFsDelay_Object((1,3,6,1,4,1,2928,6,2,16,1,1,7,1,7),_ItsIfSdiFsDelay_Type())
itsIfSdiFsDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfSdiFsDelay.setStatus(_A)
_ItsIfMonTable_Object=MibTable
itsIfMonTable=_ItsIfMonTable_Object((1,3,6,1,4,1,2928,6,2,16,1,1,9))
if mibBuilder.loadTexts:itsIfMonTable.setStatus(_A)
_ItsIfMonEntry_Object=MibTableRow
itsIfMonEntry=_ItsIfMonEntry_Object((1,3,6,1,4,1,2928,6,2,16,1,1,9,1))
itsIfMonEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:itsIfMonEntry.setStatus(_A)
class _ItsIfMonMonitoredInterface_Type(Integer32):defaultValue=0
_ItsIfMonMonitoredInterface_Type.__name__=_D
_ItsIfMonMonitoredInterface_Object=MibTableColumn
itsIfMonMonitoredInterface=_ItsIfMonMonitoredInterface_Object((1,3,6,1,4,1,2928,6,2,16,1,1,9,1,1),_ItsIfMonMonitoredInterface_Type())
itsIfMonMonitoredInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfMonMonitoredInterface.setStatus(_A)
class _ItsIfMonDirection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in',1),('out',2)))
_ItsIfMonDirection_Type.__name__=_D
_ItsIfMonDirection_Object=MibTableColumn
itsIfMonDirection=_ItsIfMonDirection_Object((1,3,6,1,4,1,2928,6,2,16,1,1,9,1,2),_ItsIfMonDirection_Type())
itsIfMonDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfMonDirection.setStatus(_A)
class _ItsIfEnableButton_Type(TruthValue):defaultValue=2
_ItsIfEnableButton_Type.__name__=_H
_ItsIfEnableButton_Object=MibTableColumn
itsIfEnableButton=_ItsIfEnableButton_Object((1,3,6,1,4,1,2928,6,2,16,1,1,9,1,3),_ItsIfEnableButton_Type())
itsIfEnableButton.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfEnableButton.setStatus(_A)
_ItsIfJ2kTable_Object=MibTable
itsIfJ2kTable=_ItsIfJ2kTable_Object((1,3,6,1,4,1,2928,6,2,16,1,1,10))
if mibBuilder.loadTexts:itsIfJ2kTable.setStatus(_A)
_ItsIfJ2kEntry_Object=MibTableRow
itsIfJ2kEntry=_ItsIfJ2kEntry_Object((1,3,6,1,4,1,2928,6,2,16,1,1,10,1))
itsIfJ2kEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:itsIfJ2kEntry.setStatus(_A)
class _ItsIfJ2kEncoderEnable_Type(TruthValue):defaultValue=2
_ItsIfJ2kEncoderEnable_Type.__name__=_H
_ItsIfJ2kEncoderEnable_Object=MibTableColumn
itsIfJ2kEncoderEnable=_ItsIfJ2kEncoderEnable_Object((1,3,6,1,4,1,2928,6,2,16,1,1,10,1,1),_ItsIfJ2kEncoderEnable_Type())
itsIfJ2kEncoderEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfJ2kEncoderEnable.setStatus(_A)
_ItsIfJ2kDecoderActive_Type=TruthValue
_ItsIfJ2kDecoderActive_Object=MibTableColumn
itsIfJ2kDecoderActive=_ItsIfJ2kDecoderActive_Object((1,3,6,1,4,1,2928,6,2,16,1,1,10,1,2),_ItsIfJ2kDecoderActive_Type())
itsIfJ2kDecoderActive.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfJ2kDecoderActive.setStatus(_A)
class _ItsIfJ2kSignalFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3,4,5,6)));namedValues=NamedValues(*((_R,0),('sdSdi',1),('hdSdiEu',3),('hdSdiUs',4),('hd3gSdiEu',5),('hd3gSdiUs',6)))
_ItsIfJ2kSignalFormat_Type.__name__=_D
_ItsIfJ2kSignalFormat_Object=MibTableColumn
itsIfJ2kSignalFormat=_ItsIfJ2kSignalFormat_Object((1,3,6,1,4,1,2928,6,2,16,1,1,10,1,3),_ItsIfJ2kSignalFormat_Type())
itsIfJ2kSignalFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfJ2kSignalFormat.setStatus(_A)
_ItsIfJ2kRateVideo_Type=Unsigned32
_ItsIfJ2kRateVideo_Object=MibTableColumn
itsIfJ2kRateVideo=_ItsIfJ2kRateVideo_Object((1,3,6,1,4,1,2928,6,2,16,1,1,10,1,4),_ItsIfJ2kRateVideo_Type())
itsIfJ2kRateVideo.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfJ2kRateVideo.setStatus(_A)
_ItsIfJ2kRateVideoMax_Type=Unsigned32
_ItsIfJ2kRateVideoMax_Object=MibTableColumn
itsIfJ2kRateVideoMax=_ItsIfJ2kRateVideoMax_Object((1,3,6,1,4,1,2928,6,2,16,1,1,10,1,5),_ItsIfJ2kRateVideoMax_Type())
itsIfJ2kRateVideoMax.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfJ2kRateVideoMax.setStatus(_A)
_ItsIfJ2kRateVbi_Type=Unsigned32
_ItsIfJ2kRateVbi_Object=MibTableColumn
itsIfJ2kRateVbi=_ItsIfJ2kRateVbi_Object((1,3,6,1,4,1,2928,6,2,16,1,1,10,1,6),_ItsIfJ2kRateVbi_Type())
itsIfJ2kRateVbi.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfJ2kRateVbi.setStatus(_A)
_ItsIfJ2kRateAnc_Type=Unsigned32
_ItsIfJ2kRateAnc_Object=MibTableColumn
itsIfJ2kRateAnc=_ItsIfJ2kRateAnc_Object((1,3,6,1,4,1,2928,6,2,16,1,1,10,1,7),_ItsIfJ2kRateAnc_Type())
itsIfJ2kRateAnc.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfJ2kRateAnc.setStatus(_A)
_ItsIfJ2kRateAudio_Type=Unsigned32
_ItsIfJ2kRateAudio_Object=MibTableColumn
itsIfJ2kRateAudio=_ItsIfJ2kRateAudio_Object((1,3,6,1,4,1,2928,6,2,16,1,1,10,1,8),_ItsIfJ2kRateAudio_Type())
itsIfJ2kRateAudio.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfJ2kRateAudio.setStatus(_A)
class _ItsIfJ2kAudioSampleSize_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(20,20),ValueRangeConstraint(24,24))
_ItsIfJ2kAudioSampleSize_Type.__name__=_G
_ItsIfJ2kAudioSampleSize_Object=MibTableColumn
itsIfJ2kAudioSampleSize=_ItsIfJ2kAudioSampleSize_Object((1,3,6,1,4,1,2928,6,2,16,1,1,10,1,9),_ItsIfJ2kAudioSampleSize_Type())
itsIfJ2kAudioSampleSize.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfJ2kAudioSampleSize.setStatus(_A)
class _ItsIfJ2kReduceAudioTransportBitrate_Type(TruthValue):defaultValue=2
_ItsIfJ2kReduceAudioTransportBitrate_Type.__name__=_H
_ItsIfJ2kReduceAudioTransportBitrate_Object=MibTableColumn
itsIfJ2kReduceAudioTransportBitrate=_ItsIfJ2kReduceAudioTransportBitrate_Object((1,3,6,1,4,1,2928,6,2,16,1,1,10,1,10),_ItsIfJ2kReduceAudioTransportBitrate_Type())
itsIfJ2kReduceAudioTransportBitrate.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfJ2kReduceAudioTransportBitrate.setStatus(_A)
_ItsIfSdiAudioTable_Object=MibTable
itsIfSdiAudioTable=_ItsIfSdiAudioTable_Object((1,3,6,1,4,1,2928,6,2,16,1,1,11))
if mibBuilder.loadTexts:itsIfSdiAudioTable.setStatus(_A)
_ItsIfSdiAudioEntry_Object=MibTableRow
itsIfSdiAudioEntry=_ItsIfSdiAudioEntry_Object((1,3,6,1,4,1,2928,6,2,16,1,1,11,1))
itsIfSdiAudioEntry.setIndexNames((0,_E,_F),(0,_E,_b))
if mibBuilder.loadTexts:itsIfSdiAudioEntry.setStatus(_A)
class _ItsIfSdiAudioIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ItsIfSdiAudioIndex_Type.__name__=_G
_ItsIfSdiAudioIndex_Object=MibTableColumn
itsIfSdiAudioIndex=_ItsIfSdiAudioIndex_Object((1,3,6,1,4,1,2928,6,2,16,1,1,11,1,1),_ItsIfSdiAudioIndex_Type())
itsIfSdiAudioIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:itsIfSdiAudioIndex.setStatus(_A)
class _ItsIfSdiAudioForward_Type(TruthValue):defaultValue=2
_ItsIfSdiAudioForward_Type.__name__=_H
_ItsIfSdiAudioForward_Object=MibTableColumn
itsIfSdiAudioForward=_ItsIfSdiAudioForward_Object((1,3,6,1,4,1,2928,6,2,16,1,1,11,1,2),_ItsIfSdiAudioForward_Type())
itsIfSdiAudioForward.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfSdiAudioForward.setStatus(_A)
_ItsIfSdiVbiTable_Object=MibTable
itsIfSdiVbiTable=_ItsIfSdiVbiTable_Object((1,3,6,1,4,1,2928,6,2,16,1,1,12))
if mibBuilder.loadTexts:itsIfSdiVbiTable.setStatus(_A)
_ItsIfSdiVbiEntry_Object=MibTableRow
itsIfSdiVbiEntry=_ItsIfSdiVbiEntry_Object((1,3,6,1,4,1,2928,6,2,16,1,1,12,1))
itsIfSdiVbiEntry.setIndexNames((0,_E,_F),(0,_E,_c))
if mibBuilder.loadTexts:itsIfSdiVbiEntry.setStatus(_A)
class _ItsIfSdiVbiIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,46))
_ItsIfSdiVbiIndex_Type.__name__=_D
_ItsIfSdiVbiIndex_Object=MibTableColumn
itsIfSdiVbiIndex=_ItsIfSdiVbiIndex_Object((1,3,6,1,4,1,2928,6,2,16,1,1,12,1,1),_ItsIfSdiVbiIndex_Type())
itsIfSdiVbiIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:itsIfSdiVbiIndex.setStatus(_A)
_ItsIfSdiVbiLineNumber_Type=Integer32
_ItsIfSdiVbiLineNumber_Object=MibTableColumn
itsIfSdiVbiLineNumber=_ItsIfSdiVbiLineNumber_Object((1,3,6,1,4,1,2928,6,2,16,1,1,12,1,2),_ItsIfSdiVbiLineNumber_Type())
itsIfSdiVbiLineNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfSdiVbiLineNumber.setStatus(_A)
class _ItsIfSdiVbiForward_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_R,0),('yes',1),(_P,2)))
_ItsIfSdiVbiForward_Type.__name__=_D
_ItsIfSdiVbiForward_Object=MibTableColumn
itsIfSdiVbiForward=_ItsIfSdiVbiForward_Object((1,3,6,1,4,1,2928,6,2,16,1,1,12,1,3),_ItsIfSdiVbiForward_Type())
itsIfSdiVbiForward.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfSdiVbiForward.setStatus(_A)
_ItsIfSdiAncTable_Object=MibTable
itsIfSdiAncTable=_ItsIfSdiAncTable_Object((1,3,6,1,4,1,2928,6,2,16,1,1,13))
if mibBuilder.loadTexts:itsIfSdiAncTable.setStatus(_A)
_ItsIfSdiAncEntry_Object=MibTableRow
itsIfSdiAncEntry=_ItsIfSdiAncEntry_Object((1,3,6,1,4,1,2928,6,2,16,1,1,13,1))
itsIfSdiAncEntry.setIndexNames((0,_E,_F),(0,_E,_d))
if mibBuilder.loadTexts:itsIfSdiAncEntry.setStatus(_A)
class _ItsIfSdiAncIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_ItsIfSdiAncIndex_Type.__name__=_D
_ItsIfSdiAncIndex_Object=MibTableColumn
itsIfSdiAncIndex=_ItsIfSdiAncIndex_Object((1,3,6,1,4,1,2928,6,2,16,1,1,13,1,1),_ItsIfSdiAncIndex_Type())
itsIfSdiAncIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:itsIfSdiAncIndex.setStatus(_A)
_ItsIfSdiAncDescription_Type=SnmpAdminString
_ItsIfSdiAncDescription_Object=MibTableColumn
itsIfSdiAncDescription=_ItsIfSdiAncDescription_Object((1,3,6,1,4,1,2928,6,2,16,1,1,13,1,2),_ItsIfSdiAncDescription_Type())
itsIfSdiAncDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfSdiAncDescription.setStatus(_A)
_ItsIfSdiAncDid_Type=Unsigned32
_ItsIfSdiAncDid_Object=MibTableColumn
itsIfSdiAncDid=_ItsIfSdiAncDid_Object((1,3,6,1,4,1,2928,6,2,16,1,1,13,1,3),_ItsIfSdiAncDid_Type())
itsIfSdiAncDid.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfSdiAncDid.setStatus(_A)
_ItsIfSdiAncSdid_Type=Unsigned32
_ItsIfSdiAncSdid_Object=MibTableColumn
itsIfSdiAncSdid=_ItsIfSdiAncSdid_Object((1,3,6,1,4,1,2928,6,2,16,1,1,13,1,4),_ItsIfSdiAncSdid_Type())
itsIfSdiAncSdid.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfSdiAncSdid.setStatus(_A)
class _ItsIfSdiAncForward_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_R,0),('yes',1),(_P,2)))
_ItsIfSdiAncForward_Type.__name__=_D
_ItsIfSdiAncForward_Object=MibTableColumn
itsIfSdiAncForward=_ItsIfSdiAncForward_Object((1,3,6,1,4,1,2928,6,2,16,1,1,13,1,5),_ItsIfSdiAncForward_Type())
itsIfSdiAncForward.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfSdiAncForward.setStatus(_A)
_ItsIfPs3Table_Object=MibTable
itsIfPs3Table=_ItsIfPs3Table_Object((1,3,6,1,4,1,2928,6,2,16,1,1,14))
if mibBuilder.loadTexts:itsIfPs3Table.setStatus(_A)
_ItsIfPs3Entry_Object=MibTableRow
itsIfPs3Entry=_ItsIfPs3Entry_Object((1,3,6,1,4,1,2928,6,2,16,1,1,14,1))
itsIfPs3Entry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:itsIfPs3Entry.setStatus(_A)
_ItsIfPs3DifferentialDelay_Type=Unsigned32
_ItsIfPs3DifferentialDelay_Object=MibTableColumn
itsIfPs3DifferentialDelay=_ItsIfPs3DifferentialDelay_Object((1,3,6,1,4,1,2928,6,2,16,1,1,14,1,1),_ItsIfPs3DifferentialDelay_Type())
itsIfPs3DifferentialDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfPs3DifferentialDelay.setStatus(_A)
_ItsIfPs3DifferentialDelayValid_Type=TruthValue
_ItsIfPs3DifferentialDelayValid_Object=MibTableColumn
itsIfPs3DifferentialDelayValid=_ItsIfPs3DifferentialDelayValid_Object((1,3,6,1,4,1,2928,6,2,16,1,1,14,1,2),_ItsIfPs3DifferentialDelayValid_Type())
itsIfPs3DifferentialDelayValid.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfPs3DifferentialDelayValid.setStatus(_A)
_ItsIfPs3AheadInterface_Type=Integer32
_ItsIfPs3AheadInterface_Object=MibTableColumn
itsIfPs3AheadInterface=_ItsIfPs3AheadInterface_Object((1,3,6,1,4,1,2928,6,2,16,1,1,14,1,3),_ItsIfPs3AheadInterface_Type())
itsIfPs3AheadInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfPs3AheadInterface.setStatus(_A)
_ItsIfPs3HitlessProtection_Type=TruthValue
_ItsIfPs3HitlessProtection_Object=MibTableColumn
itsIfPs3HitlessProtection=_ItsIfPs3HitlessProtection_Object((1,3,6,1,4,1,2928,6,2,16,1,1,14,1,4),_ItsIfPs3HitlessProtection_Type())
itsIfPs3HitlessProtection.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfPs3HitlessProtection.setStatus(_A)
_ItsIfPs3ProtectionStatus_Type=ItsProtectionStatus
_ItsIfPs3ProtectionStatus_Object=MibTableColumn
itsIfPs3ProtectionStatus=_ItsIfPs3ProtectionStatus_Object((1,3,6,1,4,1,2928,6,2,16,1,1,14,1,5),_ItsIfPs3ProtectionStatus_Type())
itsIfPs3ProtectionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:itsIfPs3ProtectionStatus.setStatus(_A)
class _ItsIfPs3ExpectedProtectionStatus_Type(ItsProtectionStatus):defaultValue=2
_ItsIfPs3ExpectedProtectionStatus_Type.__name__=_e
_ItsIfPs3ExpectedProtectionStatus_Object=MibTableColumn
itsIfPs3ExpectedProtectionStatus=_ItsIfPs3ExpectedProtectionStatus_Object((1,3,6,1,4,1,2928,6,2,16,1,1,14,1,6),_ItsIfPs3ExpectedProtectionStatus_Type())
itsIfPs3ExpectedProtectionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfPs3ExpectedProtectionStatus.setStatus(_A)
class _ItsIfPs3ForceHit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_ItsIfPs3ForceHit_Type.__name__=_G
_ItsIfPs3ForceHit_Object=MibTableColumn
itsIfPs3ForceHit=_ItsIfPs3ForceHit_Object((1,3,6,1,4,1,2928,6,2,16,1,1,14,1,7),_ItsIfPs3ForceHit_Type())
itsIfPs3ForceHit.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfPs3ForceHit.setStatus(_A)
_ItsIfPs3ActiveInterface_Type=Integer32
_ItsIfPs3ActiveInterface_Object=MibTableColumn
itsIfPs3ActiveInterface=_ItsIfPs3ActiveInterface_Object((1,3,6,1,4,1,2928,6,2,16,1,1,14,1,8),_ItsIfPs3ActiveInterface_Type())
itsIfPs3ActiveInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfPs3ActiveInterface.setStatus(_A)
_ItsIfPs3MaxExpDifferentialDelay_Type=Unsigned32
_ItsIfPs3MaxExpDifferentialDelay_Object=MibTableColumn
itsIfPs3MaxExpDifferentialDelay=_ItsIfPs3MaxExpDifferentialDelay_Object((1,3,6,1,4,1,2928,6,2,16,1,1,14,1,9),_ItsIfPs3MaxExpDifferentialDelay_Type())
itsIfPs3MaxExpDifferentialDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:itsIfPs3MaxExpDifferentialDelay.setStatus(_A)
_ItsSourceGroup_ObjectIdentity=ObjectIdentity
itsSourceGroup=_ItsSourceGroup_ObjectIdentity((1,3,6,1,4,1,2928,6,2,16,1,2))
_ItsSrcTtpLastChange_Type=TimeStamp
_ItsSrcTtpLastChange_Object=MibScalar
itsSrcTtpLastChange=_ItsSrcTtpLastChange_Object((1,3,6,1,4,1,2928,6,2,16,1,2,1),_ItsSrcTtpLastChange_Type())
itsSrcTtpLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:itsSrcTtpLastChange.setStatus(_A)
_ItsSrcTtpNextIndex_Type=Unsigned32
_ItsSrcTtpNextIndex_Object=MibScalar
itsSrcTtpNextIndex=_ItsSrcTtpNextIndex_Object((1,3,6,1,4,1,2928,6,2,16,1,2,2),_ItsSrcTtpNextIndex_Type())
itsSrcTtpNextIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:itsSrcTtpNextIndex.setStatus(_A)
_ItsSrcTtpTable_Object=MibTable
itsSrcTtpTable=_ItsSrcTtpTable_Object((1,3,6,1,4,1,2928,6,2,16,1,2,3))
if mibBuilder.loadTexts:itsSrcTtpTable.setStatus(_A)
_ItsSrcTtpEntry_Object=MibTableRow
itsSrcTtpEntry=_ItsSrcTtpEntry_Object((1,3,6,1,4,1,2928,6,2,16,1,2,3,1))
itsSrcTtpEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:itsSrcTtpEntry.setStatus(_A)
_ItsSrcTtpIndex_Type=Unsigned32
_ItsSrcTtpIndex_Object=MibTableColumn
itsSrcTtpIndex=_ItsSrcTtpIndex_Object((1,3,6,1,4,1,2928,6,2,16,1,2,3,1,1),_ItsSrcTtpIndex_Type())
itsSrcTtpIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:itsSrcTtpIndex.setStatus(_A)
_ItsSrcTtpName_Type=SnmpAdminString
_ItsSrcTtpName_Object=MibTableColumn
itsSrcTtpName=_ItsSrcTtpName_Object((1,3,6,1,4,1,2928,6,2,16,1,2,3,1,2),_ItsSrcTtpName_Type())
itsSrcTtpName.setMaxAccess(_B)
if mibBuilder.loadTexts:itsSrcTtpName.setStatus(_A)
class _ItsSrcTtpCustomerId_Type(Unsigned32):defaultValue=0
_ItsSrcTtpCustomerId_Type.__name__=_G
_ItsSrcTtpCustomerId_Object=MibTableColumn
itsSrcTtpCustomerId=_ItsSrcTtpCustomerId_Object((1,3,6,1,4,1,2928,6,2,16,1,2,3,1,3),_ItsSrcTtpCustomerId_Type())
itsSrcTtpCustomerId.setMaxAccess(_C)
if mibBuilder.loadTexts:itsSrcTtpCustomerId.setStatus(_A)
class _ItsSrcTtpPurpose_Type(SnmpAdminString):defaultHexValue=''
_ItsSrcTtpPurpose_Type.__name__=_O
_ItsSrcTtpPurpose_Object=MibTableColumn
itsSrcTtpPurpose=_ItsSrcTtpPurpose_Object((1,3,6,1,4,1,2928,6,2,16,1,2,3,1,4),_ItsSrcTtpPurpose_Type())
itsSrcTtpPurpose.setMaxAccess(_C)
if mibBuilder.loadTexts:itsSrcTtpPurpose.setStatus(_A)
_ItsSrcTtpLocalIf_Type=Unsigned32
_ItsSrcTtpLocalIf_Object=MibTableColumn
itsSrcTtpLocalIf=_ItsSrcTtpLocalIf_Object((1,3,6,1,4,1,2928,6,2,16,1,2,3,1,5),_ItsSrcTtpLocalIf_Type())
itsSrcTtpLocalIf.setMaxAccess(_C)
if mibBuilder.loadTexts:itsSrcTtpLocalIf.setStatus(_A)
_ItsSrcTtpLocalDsti_Type=Dsti
_ItsSrcTtpLocalDsti_Object=MibTableColumn
itsSrcTtpLocalDsti=_ItsSrcTtpLocalDsti_Object((1,3,6,1,4,1,2928,6,2,16,1,2,3,1,6),_ItsSrcTtpLocalDsti_Type())
itsSrcTtpLocalDsti.setMaxAccess(_C)
if mibBuilder.loadTexts:itsSrcTtpLocalDsti.setStatus(_A)
class _ItsSrcTtpMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unicast',1),(_V,2),(_W,3)))
_ItsSrcTtpMode_Type.__name__=_D
_ItsSrcTtpMode_Object=MibTableColumn
itsSrcTtpMode=_ItsSrcTtpMode_Object((1,3,6,1,4,1,2928,6,2,16,1,2,3,1,7),_ItsSrcTtpMode_Type())
itsSrcTtpMode.setMaxAccess(_S)
if mibBuilder.loadTexts:itsSrcTtpMode.setStatus(_A)
class _ItsSrcTtpODescription_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ItsSrcTtpODescription_Type.__name__=_G
_ItsSrcTtpODescription_Object=MibTableColumn
itsSrcTtpODescription=_ItsSrcTtpODescription_Object((1,3,6,1,4,1,2928,6,2,16,1,2,3,1,8),_ItsSrcTtpODescription_Type())
itsSrcTtpODescription.setMaxAccess(_B)
if mibBuilder.loadTexts:itsSrcTtpODescription.setStatus(_A)
_ItsSrcTtpOConnection_Type=Unsigned32
_ItsSrcTtpOConnection_Object=MibTableColumn
itsSrcTtpOConnection=_ItsSrcTtpOConnection_Object((1,3,6,1,4,1,2928,6,2,16,1,2,3,1,9),_ItsSrcTtpOConnection_Type())
itsSrcTtpOConnection.setMaxAccess(_B)
if mibBuilder.loadTexts:itsSrcTtpOConnection.setStatus(_A)
_ItsSrcTtpFailure_Type=SnmpAdminString
_ItsSrcTtpFailure_Object=MibTableColumn
itsSrcTtpFailure=_ItsSrcTtpFailure_Object((1,3,6,1,4,1,2928,6,2,16,1,2,3,1,10),_ItsSrcTtpFailure_Type())
itsSrcTtpFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:itsSrcTtpFailure.setStatus(_A)
class _ItsSrcTtpAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_ItsSrcTtpAdminStatus_Type.__name__=_D
_ItsSrcTtpAdminStatus_Object=MibTableColumn
itsSrcTtpAdminStatus=_ItsSrcTtpAdminStatus_Object((1,3,6,1,4,1,2928,6,2,16,1,2,3,1,11),_ItsSrcTtpAdminStatus_Type())
itsSrcTtpAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:itsSrcTtpAdminStatus.setStatus(_A)
class _ItsSrcTtpOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5,9)));namedValues=NamedValues(*((_M,1),(_N,2),(_X,4),(_Q,5),('partial',9)))
_ItsSrcTtpOperStatus_Type.__name__=_D
_ItsSrcTtpOperStatus_Object=MibTableColumn
itsSrcTtpOperStatus=_ItsSrcTtpOperStatus_Object((1,3,6,1,4,1,2928,6,2,16,1,2,3,1,12),_ItsSrcTtpOperStatus_Type())
itsSrcTtpOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:itsSrcTtpOperStatus.setStatus(_A)
_ItsSrcTtpRowStatus_Type=RowStatus
_ItsSrcTtpRowStatus_Object=MibTableColumn
itsSrcTtpRowStatus=_ItsSrcTtpRowStatus_Object((1,3,6,1,4,1,2928,6,2,16,1,2,3,1,13),_ItsSrcTtpRowStatus_Type())
itsSrcTtpRowStatus.setMaxAccess(_S)
if mibBuilder.loadTexts:itsSrcTtpRowStatus.setStatus(_A)
_ItsSrcIndexLookupTable_Object=MibTable
itsSrcIndexLookupTable=_ItsSrcIndexLookupTable_Object((1,3,6,1,4,1,2928,6,2,16,1,2,4))
if mibBuilder.loadTexts:itsSrcIndexLookupTable.setStatus(_A)
_ItsSrcIndexLookupEntry_Object=MibTableRow
itsSrcIndexLookupEntry=_ItsSrcIndexLookupEntry_Object((1,3,6,1,4,1,2928,6,2,16,1,2,4,1))
itsSrcIndexLookupEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:itsSrcIndexLookupEntry.setStatus(_A)
_ItsSrcIndexLookupIndex_Type=Unsigned32
_ItsSrcIndexLookupIndex_Object=MibTableColumn
itsSrcIndexLookupIndex=_ItsSrcIndexLookupIndex_Object((1,3,6,1,4,1,2928,6,2,16,1,2,4,1,1),_ItsSrcIndexLookupIndex_Type())
itsSrcIndexLookupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:itsSrcIndexLookupIndex.setStatus(_A)
_ItsSinkGroup_ObjectIdentity=ObjectIdentity
itsSinkGroup=_ItsSinkGroup_ObjectIdentity((1,3,6,1,4,1,2928,6,2,16,1,3))
_ItsSnkTtpLastChange_Type=TimeStamp
_ItsSnkTtpLastChange_Object=MibScalar
itsSnkTtpLastChange=_ItsSnkTtpLastChange_Object((1,3,6,1,4,1,2928,6,2,16,1,3,1),_ItsSnkTtpLastChange_Type())
itsSnkTtpLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:itsSnkTtpLastChange.setStatus(_A)
_ItsSnkTtpNextIndex_Type=Unsigned32
_ItsSnkTtpNextIndex_Object=MibScalar
itsSnkTtpNextIndex=_ItsSnkTtpNextIndex_Object((1,3,6,1,4,1,2928,6,2,16,1,3,2),_ItsSnkTtpNextIndex_Type())
itsSnkTtpNextIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:itsSnkTtpNextIndex.setStatus(_A)
_ItsSnkTtpTable_Object=MibTable
itsSnkTtpTable=_ItsSnkTtpTable_Object((1,3,6,1,4,1,2928,6,2,16,1,3,3))
if mibBuilder.loadTexts:itsSnkTtpTable.setStatus(_A)
_ItsSnkTtpEntry_Object=MibTableRow
itsSnkTtpEntry=_ItsSnkTtpEntry_Object((1,3,6,1,4,1,2928,6,2,16,1,3,3,1))
itsSnkTtpEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:itsSnkTtpEntry.setStatus(_A)
_ItsSnkTtpIndex_Type=Unsigned32
_ItsSnkTtpIndex_Object=MibTableColumn
itsSnkTtpIndex=_ItsSnkTtpIndex_Object((1,3,6,1,4,1,2928,6,2,16,1,3,3,1,1),_ItsSnkTtpIndex_Type())
itsSnkTtpIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:itsSnkTtpIndex.setStatus(_A)
_ItsSnkTtpName_Type=SnmpAdminString
_ItsSnkTtpName_Object=MibTableColumn
itsSnkTtpName=_ItsSnkTtpName_Object((1,3,6,1,4,1,2928,6,2,16,1,3,3,1,2),_ItsSnkTtpName_Type())
itsSnkTtpName.setMaxAccess(_B)
if mibBuilder.loadTexts:itsSnkTtpName.setStatus(_A)
class _ItsSnkTtpCustomerId_Type(Unsigned32):defaultValue=0
_ItsSnkTtpCustomerId_Type.__name__=_G
_ItsSnkTtpCustomerId_Object=MibTableColumn
itsSnkTtpCustomerId=_ItsSnkTtpCustomerId_Object((1,3,6,1,4,1,2928,6,2,16,1,3,3,1,3),_ItsSnkTtpCustomerId_Type())
itsSnkTtpCustomerId.setMaxAccess(_C)
if mibBuilder.loadTexts:itsSnkTtpCustomerId.setStatus(_A)
class _ItsSnkTtpPurpose_Type(SnmpAdminString):defaultHexValue=''
_ItsSnkTtpPurpose_Type.__name__=_O
_ItsSnkTtpPurpose_Object=MibTableColumn
itsSnkTtpPurpose=_ItsSnkTtpPurpose_Object((1,3,6,1,4,1,2928,6,2,16,1,3,3,1,4),_ItsSnkTtpPurpose_Type())
itsSnkTtpPurpose.setMaxAccess(_C)
if mibBuilder.loadTexts:itsSnkTtpPurpose.setStatus(_A)
_ItsSnkTtpLocalIf_Type=Unsigned32
_ItsSnkTtpLocalIf_Object=MibTableColumn
itsSnkTtpLocalIf=_ItsSnkTtpLocalIf_Object((1,3,6,1,4,1,2928,6,2,16,1,3,3,1,5),_ItsSnkTtpLocalIf_Type())
itsSnkTtpLocalIf.setMaxAccess(_C)
if mibBuilder.loadTexts:itsSnkTtpLocalIf.setStatus(_A)
_ItsSnkTtpLocalDsti_Type=Dsti
_ItsSnkTtpLocalDsti_Object=MibTableColumn
itsSnkTtpLocalDsti=_ItsSnkTtpLocalDsti_Object((1,3,6,1,4,1,2928,6,2,16,1,3,3,1,6),_ItsSnkTtpLocalDsti_Type())
itsSnkTtpLocalDsti.setMaxAccess(_C)
if mibBuilder.loadTexts:itsSnkTtpLocalDsti.setStatus(_A)
class _ItsSnkTtpPSActiveChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('primary',1),('secondary',2),(_L,3)))
_ItsSnkTtpPSActiveChannel_Type.__name__=_D
_ItsSnkTtpPSActiveChannel_Object=MibTableColumn
itsSnkTtpPSActiveChannel=_ItsSnkTtpPSActiveChannel_Object((1,3,6,1,4,1,2928,6,2,16,1,3,3,1,7),_ItsSnkTtpPSActiveChannel_Type())
itsSnkTtpPSActiveChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:itsSnkTtpPSActiveChannel.setStatus(_A)
class _ItsSnkTtpSuppressAlarm_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_K,0),(_L,1),(_U,2),('all',3)))
_ItsSnkTtpSuppressAlarm_Type.__name__=_D
_ItsSnkTtpSuppressAlarm_Object=MibTableColumn
itsSnkTtpSuppressAlarm=_ItsSnkTtpSuppressAlarm_Object((1,3,6,1,4,1,2928,6,2,16,1,3,3,1,8),_ItsSnkTtpSuppressAlarm_Type())
itsSnkTtpSuppressAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:itsSnkTtpSuppressAlarm.setStatus(_A)
_ItsSnkTtpTConnection_Type=Unsigned32
_ItsSnkTtpTConnection_Object=MibTableColumn
itsSnkTtpTConnection=_ItsSnkTtpTConnection_Object((1,3,6,1,4,1,2928,6,2,16,1,3,3,1,9),_ItsSnkTtpTConnection_Type())
itsSnkTtpTConnection.setMaxAccess(_B)
if mibBuilder.loadTexts:itsSnkTtpTConnection.setStatus(_A)
class _ItsSnkTtpDefects_Type(Bits):namedValues=NamedValues(*(('los',0),('lof',1),('ais',2),('lop',3)))
_ItsSnkTtpDefects_Type.__name__=_J
_ItsSnkTtpDefects_Object=MibTableColumn
itsSnkTtpDefects=_ItsSnkTtpDefects_Object((1,3,6,1,4,1,2928,6,2,16,1,3,3,1,10),_ItsSnkTtpDefects_Type())
itsSnkTtpDefects.setMaxAccess(_B)
if mibBuilder.loadTexts:itsSnkTtpDefects.setStatus(_A)
_ItsSnkTtpFailure_Type=SnmpAdminString
_ItsSnkTtpFailure_Object=MibTableColumn
itsSnkTtpFailure=_ItsSnkTtpFailure_Object((1,3,6,1,4,1,2928,6,2,16,1,3,3,1,11),_ItsSnkTtpFailure_Type())
itsSnkTtpFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:itsSnkTtpFailure.setStatus(_A)
_ItsSnkTtpPMReference_Type=RowPointer
_ItsSnkTtpPMReference_Object=MibTableColumn
itsSnkTtpPMReference=_ItsSnkTtpPMReference_Object((1,3,6,1,4,1,2928,6,2,16,1,3,3,1,12),_ItsSnkTtpPMReference_Type())
itsSnkTtpPMReference.setMaxAccess(_B)
if mibBuilder.loadTexts:itsSnkTtpPMReference.setStatus(_A)
class _ItsSnkTtpAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_ItsSnkTtpAdminStatus_Type.__name__=_D
_ItsSnkTtpAdminStatus_Object=MibTableColumn
itsSnkTtpAdminStatus=_ItsSnkTtpAdminStatus_Object((1,3,6,1,4,1,2928,6,2,16,1,3,3,1,13),_ItsSnkTtpAdminStatus_Type())
itsSnkTtpAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:itsSnkTtpAdminStatus.setStatus(_A)
class _ItsSnkTtpOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,5)));namedValues=NamedValues(*((_M,1),(_N,2),(_Q,5)))
_ItsSnkTtpOperStatus_Type.__name__=_D
_ItsSnkTtpOperStatus_Object=MibTableColumn
itsSnkTtpOperStatus=_ItsSnkTtpOperStatus_Object((1,3,6,1,4,1,2928,6,2,16,1,3,3,1,14),_ItsSnkTtpOperStatus_Type())
itsSnkTtpOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:itsSnkTtpOperStatus.setStatus(_A)
_ItsSnkTtpRowStatus_Type=RowStatus
_ItsSnkTtpRowStatus_Object=MibTableColumn
itsSnkTtpRowStatus=_ItsSnkTtpRowStatus_Object((1,3,6,1,4,1,2928,6,2,16,1,3,3,1,15),_ItsSnkTtpRowStatus_Type())
itsSnkTtpRowStatus.setMaxAccess(_S)
if mibBuilder.loadTexts:itsSnkTtpRowStatus.setStatus(_A)
class _ItsSnkTtpTConnection2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_ItsSnkTtpTConnection2_Type.__name__=_D
_ItsSnkTtpTConnection2_Object=MibTableColumn
itsSnkTtpTConnection2=_ItsSnkTtpTConnection2_Object((1,3,6,1,4,1,2928,6,2,16,1,3,3,1,16),_ItsSnkTtpTConnection2_Type())
itsSnkTtpTConnection2.setMaxAccess(_B)
if mibBuilder.loadTexts:itsSnkTtpTConnection2.setStatus(_A)
class _ItsSnkTtpPSAllow_Type(TruthValue):defaultValue=1
_ItsSnkTtpPSAllow_Type.__name__=_H
_ItsSnkTtpPSAllow_Object=MibTableColumn
itsSnkTtpPSAllow=_ItsSnkTtpPSAllow_Object((1,3,6,1,4,1,2928,6,2,16,1,3,3,1,17),_ItsSnkTtpPSAllow_Type())
itsSnkTtpPSAllow.setMaxAccess(_C)
if mibBuilder.loadTexts:itsSnkTtpPSAllow.setStatus(_A)
_ItsSnkIndexLookupTable_Object=MibTable
itsSnkIndexLookupTable=_ItsSnkIndexLookupTable_Object((1,3,6,1,4,1,2928,6,2,16,1,3,4))
if mibBuilder.loadTexts:itsSnkIndexLookupTable.setStatus(_A)
_ItsSnkIndexLookupEntry_Object=MibTableRow
itsSnkIndexLookupEntry=_ItsSnkIndexLookupEntry_Object((1,3,6,1,4,1,2928,6,2,16,1,3,4,1))
itsSnkIndexLookupEntry.setIndexNames((0,_E,_i))
if mibBuilder.loadTexts:itsSnkIndexLookupEntry.setStatus(_A)
_ItsSnkIndexLookupIndex_Type=Unsigned32
_ItsSnkIndexLookupIndex_Object=MibTableColumn
itsSnkIndexLookupIndex=_ItsSnkIndexLookupIndex_Object((1,3,6,1,4,1,2928,6,2,16,1,3,4,1,1),_ItsSnkIndexLookupIndex_Type())
itsSnkIndexLookupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:itsSnkIndexLookupIndex.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ItsTtpIndexList':ItsTtpIndexList,_e:ItsProtectionStatus,'netiItsMIB':netiItsMIB,'itsObjects':itsObjects,'itsIfGroup':itsIfGroup,'itsIfLastChange':itsIfLastChange,'itsIfTable':itsIfTable,'itsIfEntry':itsIfEntry,_F:itsIfIndex,'itsIfIfIndex':itsIfIfIndex,'itsIfName':itsIfName,'itsIfDescr':itsIfDescr,'itsIfSpeed':itsIfSpeed,'itsIfSuppressAlarm':itsIfSuppressAlarm,'itsIfLoopMode':itsIfLoopMode,'itsIfLoopTime':itsIfLoopTime,'itsIfCapabilities':itsIfCapabilities,'itsIfProperties':itsIfProperties,'itsIfDefects':itsIfDefects,'itsIfFailure':itsIfFailure,'itsIfPMReference':itsIfPMReference,'itsIfOperStatus':itsIfOperStatus,'itsIfTxMuteOnFault':itsIfTxMuteOnFault,'itsIfPurpose':itsIfPurpose,'itsIfInterfaceType':itsIfInterfaceType,'itsIfMembersSrc':itsIfMembersSrc,'itsIfMembersSnk':itsIfMembersSnk,'itsIfPdhTable':itsIfPdhTable,'itsIfPdhEntry':itsIfPdhEntry,'itsIfPdhSignal':itsIfPdhSignal,'itsIfPdhFraming':itsIfPdhFraming,'itsIfSdhTable':itsIfSdhTable,'itsIfSdhEntry':itsIfSdhEntry,'itsIfSdhTiming':itsIfSdhTiming,'itsIfSdhMode':itsIfSdhMode,'itsIfSdhSs':itsIfSdhSs,'itsIfSdhS1':itsIfSdhS1,'itsIfSdhSoh':itsIfSdhSoh,'itsIfSdhPoh':itsIfSdhPoh,'itsIfSdhJc':itsIfSdhJc,'itsIfDvbTable':itsIfDvbTable,'itsIfDvbEntry':itsIfDvbEntry,'itsIfDvbFormat':itsIfDvbFormat,'itsIfDvbOutputMode':itsIfDvbOutputMode,'itsIfAesTable':itsIfAesTable,'itsIfAesEntry':itsIfAesEntry,'itsIfAesIsTimingProvider':itsIfAesIsTimingProvider,'itsIfAesReference':itsIfAesReference,'itsIfSdiTable':itsIfSdiTable,'itsIfSdiEntry':itsIfSdiEntry,'itsIfSdiFormat':itsIfSdiFormat,'itsIfSdiAutoSense':itsIfSdiAutoSense,'itsIfSdiIsTimingProvider':itsIfSdiIsTimingProvider,'itsIfSdiReference':itsIfSdiReference,'itsIfSdiFsVDelay':itsIfSdiFsVDelay,'itsIfSdiFsHDelay':itsIfSdiFsHDelay,'itsIfSdiFsDelay':itsIfSdiFsDelay,'itsIfMonTable':itsIfMonTable,'itsIfMonEntry':itsIfMonEntry,'itsIfMonMonitoredInterface':itsIfMonMonitoredInterface,'itsIfMonDirection':itsIfMonDirection,'itsIfEnableButton':itsIfEnableButton,'itsIfJ2kTable':itsIfJ2kTable,'itsIfJ2kEntry':itsIfJ2kEntry,'itsIfJ2kEncoderEnable':itsIfJ2kEncoderEnable,'itsIfJ2kDecoderActive':itsIfJ2kDecoderActive,'itsIfJ2kSignalFormat':itsIfJ2kSignalFormat,'itsIfJ2kRateVideo':itsIfJ2kRateVideo,'itsIfJ2kRateVideoMax':itsIfJ2kRateVideoMax,'itsIfJ2kRateVbi':itsIfJ2kRateVbi,'itsIfJ2kRateAnc':itsIfJ2kRateAnc,'itsIfJ2kRateAudio':itsIfJ2kRateAudio,'itsIfJ2kAudioSampleSize':itsIfJ2kAudioSampleSize,'itsIfJ2kReduceAudioTransportBitrate':itsIfJ2kReduceAudioTransportBitrate,'itsIfSdiAudioTable':itsIfSdiAudioTable,'itsIfSdiAudioEntry':itsIfSdiAudioEntry,_b:itsIfSdiAudioIndex,'itsIfSdiAudioForward':itsIfSdiAudioForward,'itsIfSdiVbiTable':itsIfSdiVbiTable,'itsIfSdiVbiEntry':itsIfSdiVbiEntry,_c:itsIfSdiVbiIndex,'itsIfSdiVbiLineNumber':itsIfSdiVbiLineNumber,'itsIfSdiVbiForward':itsIfSdiVbiForward,'itsIfSdiAncTable':itsIfSdiAncTable,'itsIfSdiAncEntry':itsIfSdiAncEntry,_d:itsIfSdiAncIndex,'itsIfSdiAncDescription':itsIfSdiAncDescription,'itsIfSdiAncDid':itsIfSdiAncDid,'itsIfSdiAncSdid':itsIfSdiAncSdid,'itsIfSdiAncForward':itsIfSdiAncForward,'itsIfPs3Table':itsIfPs3Table,'itsIfPs3Entry':itsIfPs3Entry,'itsIfPs3DifferentialDelay':itsIfPs3DifferentialDelay,'itsIfPs3DifferentialDelayValid':itsIfPs3DifferentialDelayValid,'itsIfPs3AheadInterface':itsIfPs3AheadInterface,'itsIfPs3HitlessProtection':itsIfPs3HitlessProtection,'itsIfPs3ProtectionStatus':itsIfPs3ProtectionStatus,'itsIfPs3ExpectedProtectionStatus':itsIfPs3ExpectedProtectionStatus,'itsIfPs3ForceHit':itsIfPs3ForceHit,'itsIfPs3ActiveInterface':itsIfPs3ActiveInterface,'itsIfPs3MaxExpDifferentialDelay':itsIfPs3MaxExpDifferentialDelay,'itsSourceGroup':itsSourceGroup,'itsSrcTtpLastChange':itsSrcTtpLastChange,'itsSrcTtpNextIndex':itsSrcTtpNextIndex,'itsSrcTtpTable':itsSrcTtpTable,'itsSrcTtpEntry':itsSrcTtpEntry,_f:itsSrcTtpIndex,'itsSrcTtpName':itsSrcTtpName,'itsSrcTtpCustomerId':itsSrcTtpCustomerId,'itsSrcTtpPurpose':itsSrcTtpPurpose,'itsSrcTtpLocalIf':itsSrcTtpLocalIf,_g:itsSrcTtpLocalDsti,'itsSrcTtpMode':itsSrcTtpMode,'itsSrcTtpODescription':itsSrcTtpODescription,'itsSrcTtpOConnection':itsSrcTtpOConnection,'itsSrcTtpFailure':itsSrcTtpFailure,'itsSrcTtpAdminStatus':itsSrcTtpAdminStatus,'itsSrcTtpOperStatus':itsSrcTtpOperStatus,'itsSrcTtpRowStatus':itsSrcTtpRowStatus,'itsSrcIndexLookupTable':itsSrcIndexLookupTable,'itsSrcIndexLookupEntry':itsSrcIndexLookupEntry,'itsSrcIndexLookupIndex':itsSrcIndexLookupIndex,'itsSinkGroup':itsSinkGroup,'itsSnkTtpLastChange':itsSnkTtpLastChange,'itsSnkTtpNextIndex':itsSnkTtpNextIndex,'itsSnkTtpTable':itsSnkTtpTable,'itsSnkTtpEntry':itsSnkTtpEntry,_h:itsSnkTtpIndex,'itsSnkTtpName':itsSnkTtpName,'itsSnkTtpCustomerId':itsSnkTtpCustomerId,'itsSnkTtpPurpose':itsSnkTtpPurpose,'itsSnkTtpLocalIf':itsSnkTtpLocalIf,_i:itsSnkTtpLocalDsti,'itsSnkTtpPSActiveChannel':itsSnkTtpPSActiveChannel,'itsSnkTtpSuppressAlarm':itsSnkTtpSuppressAlarm,'itsSnkTtpTConnection':itsSnkTtpTConnection,'itsSnkTtpDefects':itsSnkTtpDefects,'itsSnkTtpFailure':itsSnkTtpFailure,'itsSnkTtpPMReference':itsSnkTtpPMReference,'itsSnkTtpAdminStatus':itsSnkTtpAdminStatus,'itsSnkTtpOperStatus':itsSnkTtpOperStatus,'itsSnkTtpRowStatus':itsSnkTtpRowStatus,'itsSnkTtpTConnection2':itsSnkTtpTConnection2,'itsSnkTtpPSAllow':itsSnkTtpPSAllow,'itsSnkIndexLookupTable':itsSnkIndexLookupTable,'itsSnkIndexLookupEntry':itsSnkIndexLookupEntry,'itsSnkIndexLookupIndex':itsSnkIndexLookupIndex})