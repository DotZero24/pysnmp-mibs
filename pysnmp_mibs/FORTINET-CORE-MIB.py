_h='fnNotifObjectsComplianceGroup'
_g='fnTrapsComplianceGroup'
_f='fnAdminComplianceGroup'
_e='fnMgmtComplianceGroup'
_d='fnSystemComplianceGroup'
_c='fnTrapTest'
_b='fnTrapIpChange'
_a='fnTrapFanFailure'
_Z='fnTrapIfExitBypassMode'
_Y='fnTrapIfEnterBypassMode'
_X='fnTrapAmcIfBypassMode'
_W='fnTrapPowerSupplyFailure'
_V='fnTrapVoltageOutOfRange'
_U='fnTrapTempHigh'
_T='fnTrapLogDiskThreshold'
_S='fnTrapMemThreshold'
_R='fnTrapCpuThreshold'
_Q='fnGenTrapMsg'
_P='fnAdminMask'
_O='fnAdminAddr'
_N='fnAdminAddrType'
_M='fnAdminName'
_L='fnAdminNumber'
_K='fnMgmtLanguage'
_J='fnAdminIndex'
_I='Integer32'
_H='ifIndex'
_G='IF-MIB'
_F='read-only'
_E='sysName'
_D='SNMPv2-MIB'
_C='fnSysSerial'
_B='current'
_A='FORTINET-CORE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_G,_H)
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysName,=mibBuilder.importSymbols(_D,_E)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fortinet=ModuleIdentity((1,3,6,1,4,1,12356))
if mibBuilder.loadTexts:fortinet.setRevisions(('2021-11-15 00:00','2020-01-30 00:00','2018-12-05 00:00','2018-11-05 00:00','2016-09-30 00:00','2016-05-24 00:00','2015-01-14 00:00','2014-12-10 00:00','2014-04-10 00:00','2014-03-22 00:00','2012-05-09 00:00','2012-04-23 00:00','2011-12-23 00:00','2011-04-25 00:00','2010-05-14 00:00','2009-05-20 00:00','2008-11-19 00:00','2008-10-21 00:00','2008-06-25 00:00','2008-06-16 00:00','2008-04-17 00:00'))
class FnBoolState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
class FnLanguage(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,255)));namedValues=NamedValues(*(('english',1),('simplifiedChinese',2),('japanese',3),('korean',4),('spanish',5),('traditionalChinese',6),('french',7),('portuguese',8),('undefined',255)))
class FnIndex(TextualConvention,Integer32):status=_B;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class FnSessionProto(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,6,8,12,17,22,41,46,47,50,51,89,103,108,255)));namedValues=NamedValues(*(('ip',0),('icmp',1),('igmp',2),('ipip',4),('tcp',6),('egp',8),('pup',12),('udp',17),('idp',22),('ipv6',41),('rsvp',46),('gre',47),('esp',50),('ah',51),('ospf',89),('pim',103),('comp',108),('raw',255)))
_FnCoreMib_ObjectIdentity=ObjectIdentity
fnCoreMib=_FnCoreMib_ObjectIdentity((1,3,6,1,4,1,12356,100))
_FnCommon_ObjectIdentity=ObjectIdentity
fnCommon=_FnCommon_ObjectIdentity((1,3,6,1,4,1,12356,100,1))
_FnSystem_ObjectIdentity=ObjectIdentity
fnSystem=_FnSystem_ObjectIdentity((1,3,6,1,4,1,12356,100,1,1))
_FnSysSerial_Type=DisplayString
_FnSysSerial_Object=MibScalar
fnSysSerial=_FnSysSerial_Object((1,3,6,1,4,1,12356,100,1,1,1),_FnSysSerial_Type())
fnSysSerial.setMaxAccess(_F)
if mibBuilder.loadTexts:fnSysSerial.setStatus(_B)
_FnMgmt_ObjectIdentity=ObjectIdentity
fnMgmt=_FnMgmt_ObjectIdentity((1,3,6,1,4,1,12356,100,1,2))
_FnMgmtLanguage_Type=FnLanguage
_FnMgmtLanguage_Object=MibScalar
fnMgmtLanguage=_FnMgmtLanguage_Object((1,3,6,1,4,1,12356,100,1,2,1),_FnMgmtLanguage_Type())
fnMgmtLanguage.setMaxAccess(_F)
if mibBuilder.loadTexts:fnMgmtLanguage.setStatus(_B)
_FnAdmin_ObjectIdentity=ObjectIdentity
fnAdmin=_FnAdmin_ObjectIdentity((1,3,6,1,4,1,12356,100,1,2,100))
_FnAdminNumber_Type=Integer32
_FnAdminNumber_Object=MibScalar
fnAdminNumber=_FnAdminNumber_Object((1,3,6,1,4,1,12356,100,1,2,100,1),_FnAdminNumber_Type())
fnAdminNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:fnAdminNumber.setStatus(_B)
_FnAdminTable_Object=MibTable
fnAdminTable=_FnAdminTable_Object((1,3,6,1,4,1,12356,100,1,2,100,2))
if mibBuilder.loadTexts:fnAdminTable.setStatus(_B)
_FnAdminEntry_Object=MibTableRow
fnAdminEntry=_FnAdminEntry_Object((1,3,6,1,4,1,12356,100,1,2,100,2,1))
fnAdminEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:fnAdminEntry.setStatus(_B)
class _FnAdminIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FnAdminIndex_Type.__name__=_I
_FnAdminIndex_Object=MibTableColumn
fnAdminIndex=_FnAdminIndex_Object((1,3,6,1,4,1,12356,100,1,2,100,2,1,1),_FnAdminIndex_Type())
fnAdminIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fnAdminIndex.setStatus(_B)
_FnAdminName_Type=DisplayString
_FnAdminName_Object=MibTableColumn
fnAdminName=_FnAdminName_Object((1,3,6,1,4,1,12356,100,1,2,100,2,1,2),_FnAdminName_Type())
fnAdminName.setMaxAccess(_F)
if mibBuilder.loadTexts:fnAdminName.setStatus(_B)
_FnAdminAddrType_Type=InetAddressType
_FnAdminAddrType_Object=MibTableColumn
fnAdminAddrType=_FnAdminAddrType_Object((1,3,6,1,4,1,12356,100,1,2,100,2,1,3),_FnAdminAddrType_Type())
fnAdminAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:fnAdminAddrType.setStatus(_B)
_FnAdminAddr_Type=InetAddress
_FnAdminAddr_Object=MibTableColumn
fnAdminAddr=_FnAdminAddr_Object((1,3,6,1,4,1,12356,100,1,2,100,2,1,4),_FnAdminAddr_Type())
fnAdminAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:fnAdminAddr.setStatus(_B)
_FnAdminMask_Type=InetAddressPrefixLength
_FnAdminMask_Object=MibTableColumn
fnAdminMask=_FnAdminMask_Object((1,3,6,1,4,1,12356,100,1,2,100,2,1,5),_FnAdminMask_Type())
fnAdminMask.setMaxAccess(_F)
if mibBuilder.loadTexts:fnAdminMask.setStatus(_B)
_FnTraps_ObjectIdentity=ObjectIdentity
fnTraps=_FnTraps_ObjectIdentity((1,3,6,1,4,1,12356,100,1,3))
_FnTrapsPrefix_ObjectIdentity=ObjectIdentity
fnTrapsPrefix=_FnTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,12356,100,1,3,0))
_FnTrapObjects_ObjectIdentity=ObjectIdentity
fnTrapObjects=_FnTrapObjects_ObjectIdentity((1,3,6,1,4,1,12356,100,1,3,1))
_FnGenTrapMsg_Type=DisplayString
_FnGenTrapMsg_Object=MibScalar
fnGenTrapMsg=_FnGenTrapMsg_Object((1,3,6,1,4,1,12356,100,1,3,1,1),_FnGenTrapMsg_Type())
fnGenTrapMsg.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:fnGenTrapMsg.setStatus(_B)
_FnMIBConformance_ObjectIdentity=ObjectIdentity
fnMIBConformance=_FnMIBConformance_ObjectIdentity((1,3,6,1,4,1,12356,100,10))
fnSystemComplianceGroup=ObjectGroup((1,3,6,1,4,1,12356,100,10,1))
fnSystemComplianceGroup.setObjects((_A,_C))
if mibBuilder.loadTexts:fnSystemComplianceGroup.setStatus(_B)
fnMgmtComplianceGroup=ObjectGroup((1,3,6,1,4,1,12356,100,10,2))
fnMgmtComplianceGroup.setObjects((_A,_K))
if mibBuilder.loadTexts:fnMgmtComplianceGroup.setStatus(_B)
fnAdminComplianceGroup=ObjectGroup((1,3,6,1,4,1,12356,100,10,3))
fnAdminComplianceGroup.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:fnAdminComplianceGroup.setStatus(_B)
fnNotifObjectsComplianceGroup=ObjectGroup((1,3,6,1,4,1,12356,100,10,5))
fnNotifObjectsComplianceGroup.setObjects((_A,_Q))
if mibBuilder.loadTexts:fnNotifObjectsComplianceGroup.setStatus(_B)
fnTrapCpuThreshold=NotificationType((1,3,6,1,4,1,12356,100,1,3,0,101))
fnTrapCpuThreshold.setObjects(*((_A,_C),(_D,_E)))
if mibBuilder.loadTexts:fnTrapCpuThreshold.setStatus(_B)
fnTrapMemThreshold=NotificationType((1,3,6,1,4,1,12356,100,1,3,0,102))
fnTrapMemThreshold.setObjects(*((_A,_C),(_D,_E)))
if mibBuilder.loadTexts:fnTrapMemThreshold.setStatus(_B)
fnTrapLogDiskThreshold=NotificationType((1,3,6,1,4,1,12356,100,1,3,0,103))
fnTrapLogDiskThreshold.setObjects(*((_A,_C),(_D,_E)))
if mibBuilder.loadTexts:fnTrapLogDiskThreshold.setStatus(_B)
fnTrapTempHigh=NotificationType((1,3,6,1,4,1,12356,100,1,3,0,104))
fnTrapTempHigh.setObjects(*((_A,_C),(_D,_E)))
if mibBuilder.loadTexts:fnTrapTempHigh.setStatus(_B)
fnTrapVoltageOutOfRange=NotificationType((1,3,6,1,4,1,12356,100,1,3,0,105))
fnTrapVoltageOutOfRange.setObjects(*((_A,_C),(_D,_E)))
if mibBuilder.loadTexts:fnTrapVoltageOutOfRange.setStatus(_B)
fnTrapPowerSupplyFailure=NotificationType((1,3,6,1,4,1,12356,100,1,3,0,106))
fnTrapPowerSupplyFailure.setObjects(*((_A,_C),(_D,_E)))
if mibBuilder.loadTexts:fnTrapPowerSupplyFailure.setStatus(_B)
fnTrapAmcIfBypassMode=NotificationType((1,3,6,1,4,1,12356,100,1,3,0,107))
fnTrapAmcIfBypassMode.setObjects(*((_A,_C),(_D,_E)))
if mibBuilder.loadTexts:fnTrapAmcIfBypassMode.setStatus(_B)
fnTrapFanFailure=NotificationType((1,3,6,1,4,1,12356,100,1,3,0,108))
fnTrapFanFailure.setObjects(*((_A,_C),(_D,_E)))
if mibBuilder.loadTexts:fnTrapFanFailure.setStatus(_B)
fnTrapIfEnterBypassMode=NotificationType((1,3,6,1,4,1,12356,100,1,3,0,109))
fnTrapIfEnterBypassMode.setObjects(*((_A,_C),(_D,_E)))
if mibBuilder.loadTexts:fnTrapIfEnterBypassMode.setStatus(_B)
fnTrapIfExitBypassMode=NotificationType((1,3,6,1,4,1,12356,100,1,3,0,110))
fnTrapIfExitBypassMode.setObjects(*((_A,_C),(_D,_E)))
if mibBuilder.loadTexts:fnTrapIfExitBypassMode.setStatus(_B)
fnTrapIpChange=NotificationType((1,3,6,1,4,1,12356,100,1,3,0,201))
fnTrapIpChange.setObjects(*((_A,_C),(_D,_E),(_G,_H)))
if mibBuilder.loadTexts:fnTrapIpChange.setStatus(_B)
fnTrapTest=NotificationType((1,3,6,1,4,1,12356,100,1,3,0,999))
fnTrapTest.setObjects(*((_A,_C),(_D,_E)))
if mibBuilder.loadTexts:fnTrapTest.setStatus(_B)
fnTrapsComplianceGroup=NotificationGroup((1,3,6,1,4,1,12356,100,10,4))
fnTrapsComplianceGroup.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:fnTrapsComplianceGroup.setStatus(_B)
fnMIBCompliance=ModuleCompliance((1,3,6,1,4,1,12356,100,10,100))
fnMIBCompliance.setObjects(*((_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:fnMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'FnBoolState':FnBoolState,'FnLanguage':FnLanguage,'FnIndex':FnIndex,'FnSessionProto':FnSessionProto,'fortinet':fortinet,'fnCoreMib':fnCoreMib,'fnCommon':fnCommon,'fnSystem':fnSystem,_C:fnSysSerial,'fnMgmt':fnMgmt,_K:fnMgmtLanguage,'fnAdmin':fnAdmin,_L:fnAdminNumber,'fnAdminTable':fnAdminTable,'fnAdminEntry':fnAdminEntry,_J:fnAdminIndex,_M:fnAdminName,_N:fnAdminAddrType,_O:fnAdminAddr,_P:fnAdminMask,'fnTraps':fnTraps,'fnTrapsPrefix':fnTrapsPrefix,_R:fnTrapCpuThreshold,_S:fnTrapMemThreshold,_T:fnTrapLogDiskThreshold,_U:fnTrapTempHigh,_V:fnTrapVoltageOutOfRange,_W:fnTrapPowerSupplyFailure,_X:fnTrapAmcIfBypassMode,_a:fnTrapFanFailure,_Y:fnTrapIfEnterBypassMode,_Z:fnTrapIfExitBypassMode,_b:fnTrapIpChange,_c:fnTrapTest,'fnTrapObjects':fnTrapObjects,_Q:fnGenTrapMsg,'fnMIBConformance':fnMIBConformance,_d:fnSystemComplianceGroup,_e:fnMgmtComplianceGroup,_f:fnAdminComplianceGroup,_g:fnTrapsComplianceGroup,_h:fnNotifObjectsComplianceGroup,'fnMIBCompliance':fnMIBCompliance})