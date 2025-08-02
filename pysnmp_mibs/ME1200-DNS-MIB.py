_J='me1200DnsServerStatusInfoGroup'
_I='me1200DnsGlobalsInfoGroup'
_H='me1200DnsServerStatusIpAddress'
_G='me1200DnsGlobalsProxyAdminState'
_F='me1200DnsGlobalsServerStaticVlanId'
_E='me1200DnsGlobalsServerStaticAddress'
_D='me1200DnsGlobalsServerSetting'
_C='read-write'
_B='ME1200-DNS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
me1200SwitchMgmt,=mibBuilder.importSymbols('CISCOME1200-MIB','me1200SwitchMgmt')
ME1200Unsigned16,=mibBuilder.importSymbols('ME1200-TC','ME1200Unsigned16')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
me1200DnsMib=ModuleIdentity((1,3,6,1,4,1,9,9,815,1,53))
if mibBuilder.loadTexts:me1200DnsMib.setRevisions(('2014-01-29 00:00','2013-10-30 00:00'))
class ME1200DnsServerType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('dhcp',0),('none',1),('static',2),('dhcpVlan',3)))
_Me1200DnsMIBObjects_ObjectIdentity=ObjectIdentity
me1200DnsMIBObjects=_Me1200DnsMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,53,1))
_Me1200DnsConfig_ObjectIdentity=ObjectIdentity
me1200DnsConfig=_Me1200DnsConfig_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,53,1,2))
_Me1200DnsGlobals_ObjectIdentity=ObjectIdentity
me1200DnsGlobals=_Me1200DnsGlobals_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,53,1,2,1))
_Me1200DnsGlobalsServerSetting_Type=ME1200DnsServerType
_Me1200DnsGlobalsServerSetting_Object=MibScalar
me1200DnsGlobalsServerSetting=_Me1200DnsGlobalsServerSetting_Object((1,3,6,1,4,1,9,9,815,1,53,1,2,1,1),_Me1200DnsGlobalsServerSetting_Type())
me1200DnsGlobalsServerSetting.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200DnsGlobalsServerSetting.setStatus(_A)
_Me1200DnsGlobalsServerStaticAddress_Type=IpAddress
_Me1200DnsGlobalsServerStaticAddress_Object=MibScalar
me1200DnsGlobalsServerStaticAddress=_Me1200DnsGlobalsServerStaticAddress_Object((1,3,6,1,4,1,9,9,815,1,53,1,2,1,2),_Me1200DnsGlobalsServerStaticAddress_Type())
me1200DnsGlobalsServerStaticAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200DnsGlobalsServerStaticAddress.setStatus(_A)
_Me1200DnsGlobalsServerStaticVlanId_Type=ME1200Unsigned16
_Me1200DnsGlobalsServerStaticVlanId_Object=MibScalar
me1200DnsGlobalsServerStaticVlanId=_Me1200DnsGlobalsServerStaticVlanId_Object((1,3,6,1,4,1,9,9,815,1,53,1,2,1,3),_Me1200DnsGlobalsServerStaticVlanId_Type())
me1200DnsGlobalsServerStaticVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200DnsGlobalsServerStaticVlanId.setStatus(_A)
_Me1200DnsGlobalsProxyAdminState_Type=TruthValue
_Me1200DnsGlobalsProxyAdminState_Object=MibScalar
me1200DnsGlobalsProxyAdminState=_Me1200DnsGlobalsProxyAdminState_Object((1,3,6,1,4,1,9,9,815,1,53,1,2,1,4),_Me1200DnsGlobalsProxyAdminState_Type())
me1200DnsGlobalsProxyAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200DnsGlobalsProxyAdminState.setStatus(_A)
_Me1200DnsStatus_ObjectIdentity=ObjectIdentity
me1200DnsStatus=_Me1200DnsStatus_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,53,1,3))
_Me1200DnsServerStatus_ObjectIdentity=ObjectIdentity
me1200DnsServerStatus=_Me1200DnsServerStatus_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,53,1,3,1))
_Me1200DnsServerStatusIpAddress_Type=IpAddress
_Me1200DnsServerStatusIpAddress_Object=MibScalar
me1200DnsServerStatusIpAddress=_Me1200DnsServerStatusIpAddress_Object((1,3,6,1,4,1,9,9,815,1,53,1,3,1,1),_Me1200DnsServerStatusIpAddress_Type())
me1200DnsServerStatusIpAddress.setMaxAccess('read-only')
if mibBuilder.loadTexts:me1200DnsServerStatusIpAddress.setStatus(_A)
_Me1200DnsMIBConformance_ObjectIdentity=ObjectIdentity
me1200DnsMIBConformance=_Me1200DnsMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,53,2))
_Me1200DnsMIBCompliances_ObjectIdentity=ObjectIdentity
me1200DnsMIBCompliances=_Me1200DnsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,53,2,1))
_Me1200DnsMIBGroups_ObjectIdentity=ObjectIdentity
me1200DnsMIBGroups=_Me1200DnsMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,53,2,2))
me1200DnsGlobalsInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,53,2,2,1))
me1200DnsGlobalsInfoGroup.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:me1200DnsGlobalsInfoGroup.setStatus(_A)
me1200DnsServerStatusInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,53,2,2,2))
me1200DnsServerStatusInfoGroup.setObjects((_B,_H))
if mibBuilder.loadTexts:me1200DnsServerStatusInfoGroup.setStatus(_A)
me1200DnsMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,815,1,53,2,1,1))
me1200DnsMibCompliance.setObjects(*((_B,_I),(_B,_J)))
if mibBuilder.loadTexts:me1200DnsMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ME1200DnsServerType':ME1200DnsServerType,'me1200DnsMib':me1200DnsMib,'me1200DnsMIBObjects':me1200DnsMIBObjects,'me1200DnsConfig':me1200DnsConfig,'me1200DnsGlobals':me1200DnsGlobals,_D:me1200DnsGlobalsServerSetting,_E:me1200DnsGlobalsServerStaticAddress,_F:me1200DnsGlobalsServerStaticVlanId,_G:me1200DnsGlobalsProxyAdminState,'me1200DnsStatus':me1200DnsStatus,'me1200DnsServerStatus':me1200DnsServerStatus,_H:me1200DnsServerStatusIpAddress,'me1200DnsMIBConformance':me1200DnsMIBConformance,'me1200DnsMIBCompliances':me1200DnsMIBCompliances,'me1200DnsMibCompliance':me1200DnsMibCompliance,'me1200DnsMIBGroups':me1200DnsMIBGroups,_I:me1200DnsGlobalsInfoGroup,_J:me1200DnsServerStatusInfoGroup})