_B='unknown'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
osCommonTcMib=ModuleIdentity((1,3,6,1,4,1,6926,2,6400))
if mibBuilder.loadTexts:osCommonTcMib.setRevisions(('2018-01-02 00:00',))
class OsCfmMepIdOrZero(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4095))
class EntityName(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,30))
class EntityNameOrNone(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
class BwAccountStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_B,1),('clear',2),('enabled',3),('disabled',4)))
class EntryValidator(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_B,1),('nothing',2),('delete',3),('create',4)))
class ProfileStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,5,6,9)));namedValues=NamedValues(*((_B,1),('busy',5),('free',6),('underProcessing',9)))
class PortIndex(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class PortIndexOrNone(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,2147483647))
class CfmMDLevel(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,7))
class CoS(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class ServFlowId(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4294967295))
class PortList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
class TagList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
class MepList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
class ServiceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,8,9,10,11)));namedValues=NamedValues(*((_B,1),('portBasedUni',2),('vlanBasedUni',3),('legacyEpLan',4),('legacyEvpLan',5),('vlanBasedINni',8),('portBasedINni',9),('vlanBasedENni',10),('portBasedENni',11)))
class StartTimeType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('immediate',2),('relative',3),('fixed',4)))
class RespType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_B,0),('regular',1),('generic',2)))
_Nbase_ObjectIdentity=ObjectIdentity
nbase=_Nbase_ObjectIdentity((1,3,6,1,4,1,629))
_NbSwitchG1_ObjectIdentity=ObjectIdentity
nbSwitchG1=_NbSwitchG1_ObjectIdentity((1,3,6,1,4,1,629,1))
_NbSwitchG1Il_ObjectIdentity=ObjectIdentity
nbSwitchG1Il=_NbSwitchG1Il_ObjectIdentity((1,3,6,1,4,1,629,1,50))
_Adva_ObjectIdentity=ObjectIdentity
adva=_Adva_ObjectIdentity((1,3,6,1,4,1,629,2544))
_Oaccess_ObjectIdentity=ObjectIdentity
oaccess=_Oaccess_ObjectIdentity((1,3,6,1,4,1,6926))
_OaOptiSwitch_ObjectIdentity=ObjectIdentity
oaOptiSwitch=_OaOptiSwitch_ObjectIdentity((1,3,6,1,4,1,6926,2))
mibBuilder.exportSymbols('OS-COMMON-TC-MIB',**{'OsCfmMepIdOrZero':OsCfmMepIdOrZero,'EntityName':EntityName,'EntityNameOrNone':EntityNameOrNone,'BwAccountStatus':BwAccountStatus,'EntryValidator':EntryValidator,'ProfileStatus':ProfileStatus,'PortIndex':PortIndex,'PortIndexOrNone':PortIndexOrNone,'CfmMDLevel':CfmMDLevel,'CoS':CoS,'ServFlowId':ServFlowId,'PortList':PortList,'TagList':TagList,'MepList':MepList,'ServiceType':ServiceType,'StartTimeType':StartTimeType,'RespType':RespType,'nbase':nbase,'nbSwitchG1':nbSwitchG1,'nbSwitchG1Il':nbSwitchG1Il,'adva':adva,'oaccess':oaccess,'oaOptiSwitch':oaOptiSwitch,'osCommonTcMib':osCommonTcMib})