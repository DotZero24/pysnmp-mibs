_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nortelNMIconformanceMIBs,=mibBuilder.importSymbols('NORTEL-NMI-CONFORMANCE-MIB','nortelNMIconformanceMIBs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nortelNMImibGroups=ModuleIdentity((1,3,6,1,4,1,562,29,1,2,1))
if mibBuilder.loadTexts:nortelNMImibGroups.setRevisions(('1999-06-24 00:00',))
_NortelNMIobjectGroups_ObjectIdentity=ObjectIdentity
nortelNMIobjectGroups=_NortelNMIobjectGroups_ObjectIdentity((1,3,6,1,4,1,562,29,1,2,1,1))
if mibBuilder.loadTexts:nortelNMIobjectGroups.setStatus(_A)
_NortelNMInotificationGroups_ObjectIdentity=ObjectIdentity
nortelNMInotificationGroups=_NortelNMInotificationGroups_ObjectIdentity((1,3,6,1,4,1,562,29,1,2,1,2))
if mibBuilder.loadTexts:nortelNMInotificationGroups.setStatus(_A)
mibBuilder.exportSymbols('NORTEL-NMI-GROUPS-MIB',**{'nortelNMImibGroups':nortelNMImibGroups,'nortelNMIobjectGroups':nortelNMIobjectGroups,'nortelNMInotificationGroups':nortelNMInotificationGroups})