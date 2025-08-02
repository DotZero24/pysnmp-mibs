_G='ciscoAtmSwAddrRowStatus'
_F='ciscoAtmSwAddrAddress'
_E='read-create'
_D='ciscoAtmSwAddrIndex'
_C='Integer32'
_B='CISCO-ATM-SWITCH-ADDR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoAtmSwAddrMIB=ModuleIdentity((1,3,6,1,4,1,9,9,51))
if mibBuilder.loadTexts:ciscoAtmSwAddrMIB.setRevisions(('1996-01-10 00:00',))
class AtmAddr(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(13,13),ValueSizeConstraint(20,20))
_CiscoAtmSwAddrMIBObjects_ObjectIdentity=ObjectIdentity
ciscoAtmSwAddrMIBObjects=_CiscoAtmSwAddrMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,51,1))
_CiscoAtmSwAddrTable_Object=MibTable
ciscoAtmSwAddrTable=_CiscoAtmSwAddrTable_Object((1,3,6,1,4,1,9,9,51,1,1))
if mibBuilder.loadTexts:ciscoAtmSwAddrTable.setStatus(_A)
_CiscoAtmSwAddrEntry_Object=MibTableRow
ciscoAtmSwAddrEntry=_CiscoAtmSwAddrEntry_Object((1,3,6,1,4,1,9,9,51,1,1,1))
ciscoAtmSwAddrEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:ciscoAtmSwAddrEntry.setStatus(_A)
class _CiscoAtmSwAddrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CiscoAtmSwAddrIndex_Type.__name__=_C
_CiscoAtmSwAddrIndex_Object=MibTableColumn
ciscoAtmSwAddrIndex=_CiscoAtmSwAddrIndex_Object((1,3,6,1,4,1,9,9,51,1,1,1,1),_CiscoAtmSwAddrIndex_Type())
ciscoAtmSwAddrIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ciscoAtmSwAddrIndex.setStatus(_A)
_CiscoAtmSwAddrAddress_Type=AtmAddr
_CiscoAtmSwAddrAddress_Object=MibTableColumn
ciscoAtmSwAddrAddress=_CiscoAtmSwAddrAddress_Object((1,3,6,1,4,1,9,9,51,1,1,1,2),_CiscoAtmSwAddrAddress_Type())
ciscoAtmSwAddrAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmSwAddrAddress.setStatus(_A)
_CiscoAtmSwAddrRowStatus_Type=RowStatus
_CiscoAtmSwAddrRowStatus_Object=MibTableColumn
ciscoAtmSwAddrRowStatus=_CiscoAtmSwAddrRowStatus_Object((1,3,6,1,4,1,9,9,51,1,1,1,3),_CiscoAtmSwAddrRowStatus_Type())
ciscoAtmSwAddrRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmSwAddrRowStatus.setStatus(_A)
_CiscoAtmSwAddrMIBConformance_ObjectIdentity=ObjectIdentity
ciscoAtmSwAddrMIBConformance=_CiscoAtmSwAddrMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,51,3))
_CiscoAtmSwAddrMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoAtmSwAddrMIBCompliances=_CiscoAtmSwAddrMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,51,3,1))
_CiscoAtmSwAddrMIBGroups_ObjectIdentity=ObjectIdentity
ciscoAtmSwAddrMIBGroups=_CiscoAtmSwAddrMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,51,3,2))
ciscoAtmSwAddrMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,51,3,2,1))
ciscoAtmSwAddrMIBGroup.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:ciscoAtmSwAddrMIBGroup.setStatus(_A)
ciscoAtmSwAddrMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,51,3,1,1))
if mibBuilder.loadTexts:ciscoAtmSwAddrMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AtmAddr':AtmAddr,'ciscoAtmSwAddrMIB':ciscoAtmSwAddrMIB,'ciscoAtmSwAddrMIBObjects':ciscoAtmSwAddrMIBObjects,'ciscoAtmSwAddrTable':ciscoAtmSwAddrTable,'ciscoAtmSwAddrEntry':ciscoAtmSwAddrEntry,_D:ciscoAtmSwAddrIndex,_F:ciscoAtmSwAddrAddress,_G:ciscoAtmSwAddrRowStatus,'ciscoAtmSwAddrMIBConformance':ciscoAtmSwAddrMIBConformance,'ciscoAtmSwAddrMIBCompliances':ciscoAtmSwAddrMIBCompliances,'ciscoAtmSwAddrMIBCompliance':ciscoAtmSwAddrMIBCompliance,'ciscoAtmSwAddrMIBGroups':ciscoAtmSwAddrMIBGroups,'ciscoAtmSwAddrMIBGroup':ciscoAtmSwAddrMIBGroup})