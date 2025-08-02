_I='me1200NtpConfigServerTableInfoGroup'
_H='me1200NtpConfigGlobalsInfoGroup'
_G='me1200NtpConfigServerAddress'
_F='me1200NtpConfigGlobalsMode'
_E='me1200NtpConfigServerIndex'
_D='read-write'
_C='Integer32'
_B='ME1200-NTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
me1200SwitchMgmt,=mibBuilder.importSymbols('CISCOME1200-MIB','me1200SwitchMgmt')
ME1200InetAddress,=mibBuilder.importSymbols('ME1200-TC','ME1200InetAddress')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
me1200NtpMib=ModuleIdentity((1,3,6,1,4,1,9,9,815,1,57))
if mibBuilder.loadTexts:me1200NtpMib.setRevisions(('2014-05-21 00:00',))
_Me1200NtpMibObjects_ObjectIdentity=ObjectIdentity
me1200NtpMibObjects=_Me1200NtpMibObjects_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,57,1))
_Me1200NtpConfig_ObjectIdentity=ObjectIdentity
me1200NtpConfig=_Me1200NtpConfig_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,57,1,2))
_Me1200NtpConfigGlobals_ObjectIdentity=ObjectIdentity
me1200NtpConfigGlobals=_Me1200NtpConfigGlobals_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,57,1,2,1))
_Me1200NtpConfigGlobalsMode_Type=TruthValue
_Me1200NtpConfigGlobalsMode_Object=MibScalar
me1200NtpConfigGlobalsMode=_Me1200NtpConfigGlobalsMode_Object((1,3,6,1,4,1,9,9,815,1,57,1,2,1,1),_Me1200NtpConfigGlobalsMode_Type())
me1200NtpConfigGlobalsMode.setMaxAccess(_D)
if mibBuilder.loadTexts:me1200NtpConfigGlobalsMode.setStatus(_A)
_Me1200NtpConfigServerTable_Object=MibTable
me1200NtpConfigServerTable=_Me1200NtpConfigServerTable_Object((1,3,6,1,4,1,9,9,815,1,57,1,2,2))
if mibBuilder.loadTexts:me1200NtpConfigServerTable.setStatus(_A)
_Me1200NtpConfigServerEntry_Object=MibTableRow
me1200NtpConfigServerEntry=_Me1200NtpConfigServerEntry_Object((1,3,6,1,4,1,9,9,815,1,57,1,2,2,1))
me1200NtpConfigServerEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:me1200NtpConfigServerEntry.setStatus(_A)
class _Me1200NtpConfigServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Me1200NtpConfigServerIndex_Type.__name__=_C
_Me1200NtpConfigServerIndex_Object=MibTableColumn
me1200NtpConfigServerIndex=_Me1200NtpConfigServerIndex_Object((1,3,6,1,4,1,9,9,815,1,57,1,2,2,1,1),_Me1200NtpConfigServerIndex_Type())
me1200NtpConfigServerIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:me1200NtpConfigServerIndex.setStatus(_A)
_Me1200NtpConfigServerAddress_Type=ME1200InetAddress
_Me1200NtpConfigServerAddress_Object=MibTableColumn
me1200NtpConfigServerAddress=_Me1200NtpConfigServerAddress_Object((1,3,6,1,4,1,9,9,815,1,57,1,2,2,1,2),_Me1200NtpConfigServerAddress_Type())
me1200NtpConfigServerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:me1200NtpConfigServerAddress.setStatus(_A)
_Me1200NtpMibConformance_ObjectIdentity=ObjectIdentity
me1200NtpMibConformance=_Me1200NtpMibConformance_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,57,2))
_Me1200NtpMibCompliances_ObjectIdentity=ObjectIdentity
me1200NtpMibCompliances=_Me1200NtpMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,57,2,1))
_Me1200NtpMibGroups_ObjectIdentity=ObjectIdentity
me1200NtpMibGroups=_Me1200NtpMibGroups_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,57,2,2))
me1200NtpConfigGlobalsInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,57,2,2,1))
me1200NtpConfigGlobalsInfoGroup.setObjects((_B,_F))
if mibBuilder.loadTexts:me1200NtpConfigGlobalsInfoGroup.setStatus(_A)
me1200NtpConfigServerTableInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,57,2,2,2))
me1200NtpConfigServerTableInfoGroup.setObjects((_B,_G))
if mibBuilder.loadTexts:me1200NtpConfigServerTableInfoGroup.setStatus(_A)
me1200NtpMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,815,1,57,2,1,1))
me1200NtpMibCompliance.setObjects(*((_B,_H),(_B,_I)))
if mibBuilder.loadTexts:me1200NtpMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'me1200NtpMib':me1200NtpMib,'me1200NtpMibObjects':me1200NtpMibObjects,'me1200NtpConfig':me1200NtpConfig,'me1200NtpConfigGlobals':me1200NtpConfigGlobals,_F:me1200NtpConfigGlobalsMode,'me1200NtpConfigServerTable':me1200NtpConfigServerTable,'me1200NtpConfigServerEntry':me1200NtpConfigServerEntry,_E:me1200NtpConfigServerIndex,_G:me1200NtpConfigServerAddress,'me1200NtpMibConformance':me1200NtpMibConformance,'me1200NtpMibCompliances':me1200NtpMibCompliances,'me1200NtpMibCompliance':me1200NtpMibCompliance,'me1200NtpMibGroups':me1200NtpMibGroups,_H:me1200NtpConfigGlobalsInfoGroup,_I:me1200NtpConfigServerTableInfoGroup})