_G='ciscoAtmIfAdminAddrMIBGroup'
_F='ciscoAtmIfAdminAddrRowStatus'
_E='ciscoAtmIfAdminAddrAddress'
_D='ifIndex'
_C='IF-MIB'
_B='CISCO-ATM-ADDR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoAtmAddrMIB=ModuleIdentity((1,3,6,1,4,1,9,10,12))
if mibBuilder.loadTexts:ciscoAtmAddrMIB.setRevisions(('1996-05-06 00:00',))
class AtmAddr(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(8,8),ValueSizeConstraint(13,13),ValueSizeConstraint(20,20))
_CiscoAtmAddrMIBObjects_ObjectIdentity=ObjectIdentity
ciscoAtmAddrMIBObjects=_CiscoAtmAddrMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,12,1))
_CiscoAtmIfAdminAddrTable_Object=MibTable
ciscoAtmIfAdminAddrTable=_CiscoAtmIfAdminAddrTable_Object((1,3,6,1,4,1,9,10,12,1,1))
if mibBuilder.loadTexts:ciscoAtmIfAdminAddrTable.setStatus(_A)
_CiscoAtmIfAdminAddrEntry_Object=MibTableRow
ciscoAtmIfAdminAddrEntry=_CiscoAtmIfAdminAddrEntry_Object((1,3,6,1,4,1,9,10,12,1,1,1))
ciscoAtmIfAdminAddrEntry.setIndexNames((0,_C,_D),(0,_B,_E))
if mibBuilder.loadTexts:ciscoAtmIfAdminAddrEntry.setStatus(_A)
_CiscoAtmIfAdminAddrAddress_Type=AtmAddr
_CiscoAtmIfAdminAddrAddress_Object=MibTableColumn
ciscoAtmIfAdminAddrAddress=_CiscoAtmIfAdminAddrAddress_Object((1,3,6,1,4,1,9,10,12,1,1,1,1),_CiscoAtmIfAdminAddrAddress_Type())
ciscoAtmIfAdminAddrAddress.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ciscoAtmIfAdminAddrAddress.setStatus(_A)
_CiscoAtmIfAdminAddrRowStatus_Type=RowStatus
_CiscoAtmIfAdminAddrRowStatus_Object=MibTableColumn
ciscoAtmIfAdminAddrRowStatus=_CiscoAtmIfAdminAddrRowStatus_Object((1,3,6,1,4,1,9,10,12,1,1,1,2),_CiscoAtmIfAdminAddrRowStatus_Type())
ciscoAtmIfAdminAddrRowStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:ciscoAtmIfAdminAddrRowStatus.setStatus(_A)
_CiscoAtmIfAdminAddrMIBConformance_ObjectIdentity=ObjectIdentity
ciscoAtmIfAdminAddrMIBConformance=_CiscoAtmIfAdminAddrMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,12,3))
_CiscoAtmIfAdminAddrMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoAtmIfAdminAddrMIBCompliances=_CiscoAtmIfAdminAddrMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,12,3,1))
_CiscoAtmIfAdminAddrMIBGroups_ObjectIdentity=ObjectIdentity
ciscoAtmIfAdminAddrMIBGroups=_CiscoAtmIfAdminAddrMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,12,3,2))
ciscoAtmIfAdminAddrMIBGroup=ObjectGroup((1,3,6,1,4,1,9,10,12,3,2,1))
ciscoAtmIfAdminAddrMIBGroup.setObjects((_B,_F))
if mibBuilder.loadTexts:ciscoAtmIfAdminAddrMIBGroup.setStatus(_A)
ciscoAtmIfAdminAddrMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,12,3,1,1))
ciscoAtmIfAdminAddrMIBCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:ciscoAtmIfAdminAddrMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AtmAddr':AtmAddr,'ciscoAtmAddrMIB':ciscoAtmAddrMIB,'ciscoAtmAddrMIBObjects':ciscoAtmAddrMIBObjects,'ciscoAtmIfAdminAddrTable':ciscoAtmIfAdminAddrTable,'ciscoAtmIfAdminAddrEntry':ciscoAtmIfAdminAddrEntry,_E:ciscoAtmIfAdminAddrAddress,_F:ciscoAtmIfAdminAddrRowStatus,'ciscoAtmIfAdminAddrMIBConformance':ciscoAtmIfAdminAddrMIBConformance,'ciscoAtmIfAdminAddrMIBCompliances':ciscoAtmIfAdminAddrMIBCompliances,'ciscoAtmIfAdminAddrMIBCompliance':ciscoAtmIfAdminAddrMIBCompliance,'ciscoAtmIfAdminAddrMIBGroups':ciscoAtmIfAdminAddrMIBGroups,_G:ciscoAtmIfAdminAddrMIBGroup})