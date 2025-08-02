_C='eltSnmpCommunityEntry'
_B='ELTEX-MES-SNMP-COMMUNITY-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesSnmpCommExtMIB,=mibBuilder.importSymbols('ELTEX-MES-MNG-MIB','eltMesSnmpCommExtMIB')
snmpCommunityEntry,=mibBuilder.importSymbols('SNMP-COMMUNITY-MIB','snmpCommunityEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_EltSnmpCommunityTable_Object=MibTable
eltSnmpCommunityTable=_EltSnmpCommunityTable_Object((1,3,6,1,4,1,35265,1,23,1,4,1))
if mibBuilder.loadTexts:eltSnmpCommunityTable.setStatus(_A)
_EltSnmpCommunityEntry_Object=MibTableRow
eltSnmpCommunityEntry=_EltSnmpCommunityEntry_Object((1,3,6,1,4,1,35265,1,23,1,4,1,1))
if mibBuilder.loadTexts:eltSnmpCommunityEntry.setStatus(_A)
_EltSnmpCommunityAccessList_Type=Integer32
_EltSnmpCommunityAccessList_Object=MibTableColumn
eltSnmpCommunityAccessList=_EltSnmpCommunityAccessList_Object((1,3,6,1,4,1,35265,1,23,1,4,1,1,1),_EltSnmpCommunityAccessList_Type())
eltSnmpCommunityAccessList.setMaxAccess('read-create')
if mibBuilder.loadTexts:eltSnmpCommunityAccessList.setStatus(_A)
snmpCommunityEntry.registerAugmentions((_B,_C))
eltSnmpCommunityEntry.setIndexNames(*snmpCommunityEntry.getIndexNames())
mibBuilder.exportSymbols(_B,**{'eltSnmpCommunityTable':eltSnmpCommunityTable,_C:eltSnmpCommunityEntry,'eltSnmpCommunityAccessList':eltSnmpCommunityAccessList})