_I='cie1000NtpConfigServerTableInfoGroup'
_H='cie1000NtpConfigGlobalsInfoGroup'
_G='cie1000NtpConfigServerAddress'
_F='cie1000NtpConfigGlobalsMode'
_E='read-write'
_D='Integer32'
_C='cie1000NtpConfigServerIndex'
_B='CIE1000-NTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CIE1000InetAddress,=mibBuilder.importSymbols('CIE1000-TC','CIE1000InetAddress')
cie1000SwitchMgmt,=mibBuilder.importSymbols('CISCO-IE1000-MIB','cie1000SwitchMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
cie1000NtpMib=ModuleIdentity((1,3,6,1,4,1,9,9,832,1,57))
if mibBuilder.loadTexts:cie1000NtpMib.setRevisions(('2014-10-10 00:00','2014-07-01 00:00'))
_Cie1000NtpMibObjects_ObjectIdentity=ObjectIdentity
cie1000NtpMibObjects=_Cie1000NtpMibObjects_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,57,1))
_Cie1000NtpConfig_ObjectIdentity=ObjectIdentity
cie1000NtpConfig=_Cie1000NtpConfig_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,57,1,2))
_Cie1000NtpConfigGlobals_ObjectIdentity=ObjectIdentity
cie1000NtpConfigGlobals=_Cie1000NtpConfigGlobals_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,57,1,2,1))
_Cie1000NtpConfigGlobalsMode_Type=TruthValue
_Cie1000NtpConfigGlobalsMode_Object=MibScalar
cie1000NtpConfigGlobalsMode=_Cie1000NtpConfigGlobalsMode_Object((1,3,6,1,4,1,9,9,832,1,57,1,2,1,1),_Cie1000NtpConfigGlobalsMode_Type())
cie1000NtpConfigGlobalsMode.setMaxAccess(_E)
if mibBuilder.loadTexts:cie1000NtpConfigGlobalsMode.setStatus(_A)
_Cie1000NtpConfigServerTable_Object=MibTable
cie1000NtpConfigServerTable=_Cie1000NtpConfigServerTable_Object((1,3,6,1,4,1,9,9,832,1,57,1,2,2))
if mibBuilder.loadTexts:cie1000NtpConfigServerTable.setStatus(_A)
_Cie1000NtpConfigServerEntry_Object=MibTableRow
cie1000NtpConfigServerEntry=_Cie1000NtpConfigServerEntry_Object((1,3,6,1,4,1,9,9,832,1,57,1,2,2,1))
cie1000NtpConfigServerEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:cie1000NtpConfigServerEntry.setStatus(_A)
class _Cie1000NtpConfigServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Cie1000NtpConfigServerIndex_Type.__name__=_D
_Cie1000NtpConfigServerIndex_Object=MibTableColumn
cie1000NtpConfigServerIndex=_Cie1000NtpConfigServerIndex_Object((1,3,6,1,4,1,9,9,832,1,57,1,2,2,1,1),_Cie1000NtpConfigServerIndex_Type())
cie1000NtpConfigServerIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:cie1000NtpConfigServerIndex.setStatus(_A)
_Cie1000NtpConfigServerAddress_Type=CIE1000InetAddress
_Cie1000NtpConfigServerAddress_Object=MibTableColumn
cie1000NtpConfigServerAddress=_Cie1000NtpConfigServerAddress_Object((1,3,6,1,4,1,9,9,832,1,57,1,2,2,1,2),_Cie1000NtpConfigServerAddress_Type())
cie1000NtpConfigServerAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:cie1000NtpConfigServerAddress.setStatus(_A)
_Cie1000NtpMibConformance_ObjectIdentity=ObjectIdentity
cie1000NtpMibConformance=_Cie1000NtpMibConformance_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,57,2))
_Cie1000NtpMibCompliances_ObjectIdentity=ObjectIdentity
cie1000NtpMibCompliances=_Cie1000NtpMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,57,2,1))
_Cie1000NtpMibGroups_ObjectIdentity=ObjectIdentity
cie1000NtpMibGroups=_Cie1000NtpMibGroups_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,57,2,2))
cie1000NtpConfigGlobalsInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,832,1,57,2,2,1))
cie1000NtpConfigGlobalsInfoGroup.setObjects((_B,_F))
if mibBuilder.loadTexts:cie1000NtpConfigGlobalsInfoGroup.setStatus(_A)
cie1000NtpConfigServerTableInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,832,1,57,2,2,2))
cie1000NtpConfigServerTableInfoGroup.setObjects(*((_B,_C),(_B,_G)))
if mibBuilder.loadTexts:cie1000NtpConfigServerTableInfoGroup.setStatus(_A)
cie1000NtpMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,832,1,57,2,1,1))
cie1000NtpMibCompliance.setObjects(*((_B,_H),(_B,_I)))
if mibBuilder.loadTexts:cie1000NtpMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cie1000NtpMib':cie1000NtpMib,'cie1000NtpMibObjects':cie1000NtpMibObjects,'cie1000NtpConfig':cie1000NtpConfig,'cie1000NtpConfigGlobals':cie1000NtpConfigGlobals,_F:cie1000NtpConfigGlobalsMode,'cie1000NtpConfigServerTable':cie1000NtpConfigServerTable,'cie1000NtpConfigServerEntry':cie1000NtpConfigServerEntry,_C:cie1000NtpConfigServerIndex,_G:cie1000NtpConfigServerAddress,'cie1000NtpMibConformance':cie1000NtpMibConformance,'cie1000NtpMibCompliances':cie1000NtpMibCompliances,'cie1000NtpMibCompliance':cie1000NtpMibCompliance,'cie1000NtpMibGroups':cie1000NtpMibGroups,_H:cie1000NtpConfigGlobalsInfoGroup,_I:cie1000NtpConfigServerTableInfoGroup})