_J='snmpTrapIndex'
_I='read-create'
_H='not-accessible'
_G='snmpCommunityIndex'
_F='DisplayString'
_E='IpAddress'
_D='SUPERMICRO-SNMPv2-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,_E,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
futuresnmp=ModuleIdentity((1,3,6,1,4,1,10876,101,1,50))
if mibBuilder.loadTexts:futuresnmp.setRevisions(('2012-09-05 00:00',))
class EntryStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('valid',1),('createRequest',2),('underCreation',3),('invalid',4)))
class _SnmpListenPort_Type(Integer32):defaultValue=161;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SnmpListenPort_Type.__name__=_C
_SnmpListenPort_Object=MibScalar
snmpListenPort=_SnmpListenPort_Object((1,3,6,1,4,1,10876,101,1,50,1),_SnmpListenPort_Type())
snmpListenPort.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpListenPort.setStatus(_A)
class _SnmpListenTrapPort_Type(Integer32):defaultValue=162;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SnmpListenTrapPort_Type.__name__=_C
_SnmpListenTrapPort_Object=MibScalar
snmpListenTrapPort=_SnmpListenTrapPort_Object((1,3,6,1,4,1,10876,101,1,50,2),_SnmpListenTrapPort_Type())
snmpListenTrapPort.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpListenTrapPort.setStatus(_A)
_SnmpCommunityTable_Object=MibTable
snmpCommunityTable=_SnmpCommunityTable_Object((1,3,6,1,4,1,10876,101,1,50,3))
if mibBuilder.loadTexts:snmpCommunityTable.setStatus(_A)
_SnmpCommunityEntry_Object=MibTableRow
snmpCommunityEntry=_SnmpCommunityEntry_Object((1,3,6,1,4,1,10876,101,1,50,3,1))
snmpCommunityEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:snmpCommunityEntry.setStatus(_A)
class _SnmpCommunityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_SnmpCommunityIndex_Type.__name__=_C
_SnmpCommunityIndex_Object=MibTableColumn
snmpCommunityIndex=_SnmpCommunityIndex_Object((1,3,6,1,4,1,10876,101,1,50,3,1,1),_SnmpCommunityIndex_Type())
snmpCommunityIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:snmpCommunityIndex.setStatus(_A)
_SnmpCommunityName_Type=DisplayString
_SnmpCommunityName_Object=MibTableColumn
snmpCommunityName=_SnmpCommunityName_Object((1,3,6,1,4,1,10876,101,1,50,3,1,2),_SnmpCommunityName_Type())
snmpCommunityName.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpCommunityName.setStatus(_A)
class _SnmpCommunityPrivilege_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('readonly',1),('readwrite',2)))
_SnmpCommunityPrivilege_Type.__name__=_C
_SnmpCommunityPrivilege_Object=MibTableColumn
snmpCommunityPrivilege=_SnmpCommunityPrivilege_Object((1,3,6,1,4,1,10876,101,1,50,3,1,3),_SnmpCommunityPrivilege_Type())
snmpCommunityPrivilege.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpCommunityPrivilege.setStatus(_A)
class _SnmpCommunityIpAddr_Type(IpAddress):defaultHexValue='00000000'
_SnmpCommunityIpAddr_Type.__name__=_E
_SnmpCommunityIpAddr_Object=MibTableColumn
snmpCommunityIpAddr=_SnmpCommunityIpAddr_Object((1,3,6,1,4,1,10876,101,1,50,3,1,4),_SnmpCommunityIpAddr_Type())
snmpCommunityIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpCommunityIpAddr.setStatus(_A)
_SnmpStatus_Type=EntryStatus
_SnmpStatus_Object=MibTableColumn
snmpStatus=_SnmpStatus_Object((1,3,6,1,4,1,10876,101,1,50,3,1,5),_SnmpStatus_Type())
snmpStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:snmpStatus.setStatus(_A)
_SnmpTrapTable_Object=MibTable
snmpTrapTable=_SnmpTrapTable_Object((1,3,6,1,4,1,10876,101,1,50,4))
if mibBuilder.loadTexts:snmpTrapTable.setStatus(_A)
_SnmpTrapEntry_Object=MibTableRow
snmpTrapEntry=_SnmpTrapEntry_Object((1,3,6,1,4,1,10876,101,1,50,4,1))
snmpTrapEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:snmpTrapEntry.setStatus(_A)
class _SnmpTrapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_SnmpTrapIndex_Type.__name__=_C
_SnmpTrapIndex_Object=MibTableColumn
snmpTrapIndex=_SnmpTrapIndex_Object((1,3,6,1,4,1,10876,101,1,50,4,1,1),_SnmpTrapIndex_Type())
snmpTrapIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:snmpTrapIndex.setStatus(_A)
class _SnmpTrapCommunityName_Type(DisplayString):defaultValue=OctetString('PUBLIC')
_SnmpTrapCommunityName_Type.__name__=_F
_SnmpTrapCommunityName_Object=MibTableColumn
snmpTrapCommunityName=_SnmpTrapCommunityName_Object((1,3,6,1,4,1,10876,101,1,50,4,1,2),_SnmpTrapCommunityName_Type())
snmpTrapCommunityName.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpTrapCommunityName.setStatus(_A)
_SnmpTrapIpAddr_Type=IpAddress
_SnmpTrapIpAddr_Object=MibTableColumn
snmpTrapIpAddr=_SnmpTrapIpAddr_Object((1,3,6,1,4,1,10876,101,1,50,4,1,3),_SnmpTrapIpAddr_Type())
snmpTrapIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpTrapIpAddr.setStatus(_A)
class _SnmpTrapMgrType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('v1',0),('v2',1),('v1v2',2)))
_SnmpTrapMgrType_Type.__name__=_C
_SnmpTrapMgrType_Object=MibTableColumn
snmpTrapMgrType=_SnmpTrapMgrType_Object((1,3,6,1,4,1,10876,101,1,50,4,1,4),_SnmpTrapMgrType_Type())
snmpTrapMgrType.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpTrapMgrType.setStatus(_A)
_SnmpTrapStatus_Type=EntryStatus
_SnmpTrapStatus_Object=MibTableColumn
snmpTrapStatus=_SnmpTrapStatus_Object((1,3,6,1,4,1,10876,101,1,50,4,1,5),_SnmpTrapStatus_Type())
snmpTrapStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:snmpTrapStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'EntryStatus':EntryStatus,'futuresnmp':futuresnmp,'snmpListenPort':snmpListenPort,'snmpListenTrapPort':snmpListenTrapPort,'snmpCommunityTable':snmpCommunityTable,'snmpCommunityEntry':snmpCommunityEntry,_G:snmpCommunityIndex,'snmpCommunityName':snmpCommunityName,'snmpCommunityPrivilege':snmpCommunityPrivilege,'snmpCommunityIpAddr':snmpCommunityIpAddr,'snmpStatus':snmpStatus,'snmpTrapTable':snmpTrapTable,'snmpTrapEntry':snmpTrapEntry,_J:snmpTrapIndex,'snmpTrapCommunityName':snmpTrapCommunityName,'snmpTrapIpAddr':snmpTrapIpAddr,'snmpTrapMgrType':snmpTrapMgrType,'snmpTrapStatus':snmpTrapStatus})