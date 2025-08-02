_G='protocolName'
_F='templateProtocolName'
_E='TPLINK-PROTOCOL-VLAN-MIB'
_D='Integer32'
_C='OctetString'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkProtocolVlanMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,16))
if mibBuilder.loadTexts:tplinkProtocolVlanMIB.setRevisions(('2009-08-03 00:00',))
_TplinkProtocolVlanMIBObjects_ObjectIdentity=ObjectIdentity
tplinkProtocolVlanMIBObjects=_TplinkProtocolVlanMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,16,1))
_ProtocolTemplate_ObjectIdentity=ObjectIdentity
protocolTemplate=_ProtocolTemplate_ObjectIdentity((1,3,6,1,4,1,11863,6,16,1,1))
_ProtocolTemplateTable_Object=MibTable
protocolTemplateTable=_ProtocolTemplateTable_Object((1,3,6,1,4,1,11863,6,16,1,1,1))
if mibBuilder.loadTexts:protocolTemplateTable.setStatus(_A)
_TemplateEntry_Object=MibTableRow
templateEntry=_TemplateEntry_Object((1,3,6,1,4,1,11863,6,16,1,1,1,1))
templateEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:templateEntry.setStatus(_A)
class _TemplateProtocolName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TemplateProtocolName_Type.__name__=_C
_TemplateProtocolName_Object=MibTableColumn
templateProtocolName=_TemplateProtocolName_Object((1,3,6,1,4,1,11863,6,16,1,1,1,1,1),_TemplateProtocolName_Type())
templateProtocolName.setMaxAccess(_B)
if mibBuilder.loadTexts:templateProtocolName.setStatus(_A)
class _TemplateEtherType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_TemplateEtherType_Type.__name__=_C
_TemplateEtherType_Object=MibTableColumn
templateEtherType=_TemplateEtherType_Object((1,3,6,1,4,1,11863,6,16,1,1,1,1,2),_TemplateEtherType_Type())
templateEtherType.setMaxAccess(_B)
if mibBuilder.loadTexts:templateEtherType.setStatus(_A)
class _TemplateFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('ethernet8023',0),('ethernetII',1),('snap',2),('llc',3)))
_TemplateFrameType_Type.__name__=_D
_TemplateFrameType_Object=MibTableColumn
templateFrameType=_TemplateFrameType_Object((1,3,6,1,4,1,11863,6,16,1,1,1,1,3),_TemplateFrameType_Type())
templateFrameType.setMaxAccess(_B)
if mibBuilder.loadTexts:templateFrameType.setStatus(_A)
_TemplateStatus_Type=TPRowStatus
_TemplateStatus_Object=MibTableColumn
templateStatus=_TemplateStatus_Object((1,3,6,1,4,1,11863,6,16,1,1,1,1,4),_TemplateStatus_Type())
templateStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:templateStatus.setStatus(_A)
_ProtocolGroup_ObjectIdentity=ObjectIdentity
protocolGroup=_ProtocolGroup_ObjectIdentity((1,3,6,1,4,1,11863,6,16,1,2))
_ProtocolGroupTable_Object=MibTable
protocolGroupTable=_ProtocolGroupTable_Object((1,3,6,1,4,1,11863,6,16,1,2,1))
if mibBuilder.loadTexts:protocolGroupTable.setStatus(_A)
_ProtocolVlanEntry_Object=MibTableRow
protocolVlanEntry=_ProtocolVlanEntry_Object((1,3,6,1,4,1,11863,6,16,1,2,1,1))
protocolVlanEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:protocolVlanEntry.setStatus(_A)
class _ProtocolName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ProtocolName_Type.__name__=_C
_ProtocolName_Object=MibTableColumn
protocolName=_ProtocolName_Object((1,3,6,1,4,1,11863,6,16,1,2,1,1,1),_ProtocolName_Type())
protocolName.setMaxAccess('read-only')
if mibBuilder.loadTexts:protocolName.setStatus(_A)
class _ProtocolVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ProtocolVlanId_Type.__name__=_D
_ProtocolVlanId_Object=MibTableColumn
protocolVlanId=_ProtocolVlanId_Object((1,3,6,1,4,1,11863,6,16,1,2,1,1,2),_ProtocolVlanId_Type())
protocolVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:protocolVlanId.setStatus(_A)
class _ProtocolPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ProtocolPriority_Type.__name__=_D
_ProtocolPriority_Object=MibTableColumn
protocolPriority=_ProtocolPriority_Object((1,3,6,1,4,1,11863,6,16,1,2,1,1,3),_ProtocolPriority_Type())
protocolPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:protocolPriority.setStatus(_A)
_ProtocolPortMember_Type=OctetString
_ProtocolPortMember_Object=MibTableColumn
protocolPortMember=_ProtocolPortMember_Object((1,3,6,1,4,1,11863,6,16,1,2,1,1,4),_ProtocolPortMember_Type())
protocolPortMember.setMaxAccess(_B)
if mibBuilder.loadTexts:protocolPortMember.setStatus(_A)
_ProtocolVlanStatus_Type=TPRowStatus
_ProtocolVlanStatus_Object=MibTableColumn
protocolVlanStatus=_ProtocolVlanStatus_Object((1,3,6,1,4,1,11863,6,16,1,2,1,1,5),_ProtocolVlanStatus_Type())
protocolVlanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:protocolVlanStatus.setStatus(_A)
_TplinkProtocolVlanNotifications_ObjectIdentity=ObjectIdentity
tplinkProtocolVlanNotifications=_TplinkProtocolVlanNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,16,2))
mibBuilder.exportSymbols(_E,**{'tplinkProtocolVlanMIB':tplinkProtocolVlanMIB,'tplinkProtocolVlanMIBObjects':tplinkProtocolVlanMIBObjects,'protocolTemplate':protocolTemplate,'protocolTemplateTable':protocolTemplateTable,'templateEntry':templateEntry,_F:templateProtocolName,'templateEtherType':templateEtherType,'templateFrameType':templateFrameType,'templateStatus':templateStatus,'protocolGroup':protocolGroup,'protocolGroupTable':protocolGroupTable,'protocolVlanEntry':protocolVlanEntry,_G:protocolName,'protocolVlanId':protocolVlanId,'protocolPriority':protocolPriority,'protocolPortMember':protocolPortMember,'protocolVlanStatus':protocolVlanStatus,'tplinkProtocolVlanNotifications':tplinkProtocolVlanNotifications})