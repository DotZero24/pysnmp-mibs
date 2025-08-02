_E='sdmTemName'
_D='TPLINK-SDM-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkSDMMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,90))
if mibBuilder.loadTexts:tplinkSDMMIB.setRevisions(('2012-12-13 09:30',))
_TplinkSDMMIBObjects_ObjectIdentity=ObjectIdentity
tplinkSDMMIBObjects=_TplinkSDMMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,90,1))
_SdmTemLayOutTable_Object=MibTable
sdmTemLayOutTable=_SdmTemLayOutTable_Object((1,3,6,1,4,1,11863,6,90,1,1))
if mibBuilder.loadTexts:sdmTemLayOutTable.setStatus(_A)
_SdmTemLayOutEntry_Object=MibTableRow
sdmTemLayOutEntry=_SdmTemLayOutEntry_Object((1,3,6,1,4,1,11863,6,90,1,1,1))
sdmTemLayOutEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:sdmTemLayOutEntry.setStatus(_A)
_SdmTemName_Type=DisplayString
_SdmTemName_Object=MibTableColumn
sdmTemName=_SdmTemName_Object((1,3,6,1,4,1,11863,6,90,1,1,1,1),_SdmTemName_Type())
sdmTemName.setMaxAccess(_B)
if mibBuilder.loadTexts:sdmTemName.setStatus(_A)
_IpAclRuleNum_Type=Integer32
_IpAclRuleNum_Object=MibTableColumn
ipAclRuleNum=_IpAclRuleNum_Object((1,3,6,1,4,1,11863,6,90,1,1,1,2),_IpAclRuleNum_Type())
ipAclRuleNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ipAclRuleNum.setStatus(_A)
_MacAclRuleNum_Type=Integer32
_MacAclRuleNum_Object=MibTableColumn
macAclRuleNum=_MacAclRuleNum_Object((1,3,6,1,4,1,11863,6,90,1,1,1,3),_MacAclRuleNum_Type())
macAclRuleNum.setMaxAccess(_B)
if mibBuilder.loadTexts:macAclRuleNum.setStatus(_A)
_CombinedAclRuleNum_Type=Integer32
_CombinedAclRuleNum_Object=MibTableColumn
combinedAclRuleNum=_CombinedAclRuleNum_Object((1,3,6,1,4,1,11863,6,90,1,1,1,4),_CombinedAclRuleNum_Type())
combinedAclRuleNum.setMaxAccess(_B)
if mibBuilder.loadTexts:combinedAclRuleNum.setStatus(_A)
_Ipv6AclRuleNum_Type=Integer32
_Ipv6AclRuleNum_Object=MibTableColumn
ipv6AclRuleNum=_Ipv6AclRuleNum_Object((1,3,6,1,4,1,11863,6,90,1,1,1,5),_Ipv6AclRuleNum_Type())
ipv6AclRuleNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv6AclRuleNum.setStatus(_A)
_V4SourceNum_Type=Integer32
_V4SourceNum_Object=MibTableColumn
v4SourceNum=_V4SourceNum_Object((1,3,6,1,4,1,11863,6,90,1,1,1,6),_V4SourceNum_Type())
v4SourceNum.setMaxAccess(_B)
if mibBuilder.loadTexts:v4SourceNum.setStatus(_A)
_V6SourceNum_Type=Integer32
_V6SourceNum_Object=MibTableColumn
v6SourceNum=_V6SourceNum_Object((1,3,6,1,4,1,11863,6,90,1,1,1,7),_V6SourceNum_Type())
v6SourceNum.setMaxAccess(_B)
if mibBuilder.loadTexts:v6SourceNum.setStatus(_A)
_PacketContentAclNum_Type=Integer32
_PacketContentAclNum_Object=MibTableColumn
packetContentAclNum=_PacketContentAclNum_Object((1,3,6,1,4,1,11863,6,90,1,1,1,8),_PacketContentAclNum_Type())
packetContentAclNum.setMaxAccess(_B)
if mibBuilder.loadTexts:packetContentAclNum.setStatus(_A)
_SdmCurTemName_Type=DisplayString
_SdmCurTemName_Object=MibScalar
sdmCurTemName=_SdmCurTemName_Object((1,3,6,1,4,1,11863,6,90,1,2),_SdmCurTemName_Type())
sdmCurTemName.setMaxAccess(_B)
if mibBuilder.loadTexts:sdmCurTemName.setStatus(_A)
class _SdmNextTemID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('default',0),('enterpriseV4',1),('enterpriseV6',2)))
_SdmNextTemID_Type.__name__=_C
_SdmNextTemID_Object=MibScalar
sdmNextTemID=_SdmNextTemID_Object((1,3,6,1,4,1,11863,6,90,1,3),_SdmNextTemID_Type())
sdmNextTemID.setMaxAccess('read-write')
if mibBuilder.loadTexts:sdmNextTemID.setStatus(_A)
_TplinkSDMNotifications_ObjectIdentity=ObjectIdentity
tplinkSDMNotifications=_TplinkSDMNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,90,2))
mibBuilder.exportSymbols(_D,**{'tplinkSDMMIB':tplinkSDMMIB,'tplinkSDMMIBObjects':tplinkSDMMIBObjects,'sdmTemLayOutTable':sdmTemLayOutTable,'sdmTemLayOutEntry':sdmTemLayOutEntry,_E:sdmTemName,'ipAclRuleNum':ipAclRuleNum,'macAclRuleNum':macAclRuleNum,'combinedAclRuleNum':combinedAclRuleNum,'ipv6AclRuleNum':ipv6AclRuleNum,'v4SourceNum':v4SourceNum,'v6SourceNum':v6SourceNum,'packetContentAclNum':packetContentAclNum,'sdmCurTemName':sdmCurTemName,'sdmNextTemID':sdmNextTemID,'tplinkSDMNotifications':tplinkSDMNotifications})