_L='pdnAtmBridgeIwfGroup'
_K='pdnAtmBridgeIwfDot1dBasePort'
_J='pdnAtmBridgeIwfRowStatus'
_I='read-create'
_H='not-accessible'
_G='pdnAtmBridgeIwfVclVci'
_F='pdnAtmBridgeIwfVclVpi'
_E='ifIndex'
_D='IF-MIB'
_C='Unsigned32'
_B='PDN-ATM-BRIDGE-IWF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
pdn_common,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-common')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
pdnAtmBridgeIwfMIB=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,43))
if mibBuilder.loadTexts:pdnAtmBridgeIwfMIB.setRevisions(('2003-04-24 00:00','2003-03-24 00:00','2003-03-17 00:00'))
_PdnAtmBridgeIwfNotifications_ObjectIdentity=ObjectIdentity
pdnAtmBridgeIwfNotifications=_PdnAtmBridgeIwfNotifications_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,43,0))
_PdnAtmBridgeIwfObjects_ObjectIdentity=ObjectIdentity
pdnAtmBridgeIwfObjects=_PdnAtmBridgeIwfObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,43,1))
_PdnAtmBridgeIwfTable_Object=MibTable
pdnAtmBridgeIwfTable=_PdnAtmBridgeIwfTable_Object((1,3,6,1,4,1,1795,2,24,2,43,1,1))
if mibBuilder.loadTexts:pdnAtmBridgeIwfTable.setStatus(_A)
_PdnAtmBridgeIwfEntry_Object=MibTableRow
pdnAtmBridgeIwfEntry=_PdnAtmBridgeIwfEntry_Object((1,3,6,1,4,1,1795,2,24,2,43,1,1,1))
pdnAtmBridgeIwfEntry.setIndexNames((0,_D,_E),(0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:pdnAtmBridgeIwfEntry.setStatus(_A)
class _PdnAtmBridgeIwfVclVpi_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_PdnAtmBridgeIwfVclVpi_Type.__name__=_C
_PdnAtmBridgeIwfVclVpi_Object=MibTableColumn
pdnAtmBridgeIwfVclVpi=_PdnAtmBridgeIwfVclVpi_Object((1,3,6,1,4,1,1795,2,24,2,43,1,1,1,1),_PdnAtmBridgeIwfVclVpi_Type())
pdnAtmBridgeIwfVclVpi.setMaxAccess(_H)
if mibBuilder.loadTexts:pdnAtmBridgeIwfVclVpi.setStatus(_A)
class _PdnAtmBridgeIwfVclVci_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PdnAtmBridgeIwfVclVci_Type.__name__=_C
_PdnAtmBridgeIwfVclVci_Object=MibTableColumn
pdnAtmBridgeIwfVclVci=_PdnAtmBridgeIwfVclVci_Object((1,3,6,1,4,1,1795,2,24,2,43,1,1,1,2),_PdnAtmBridgeIwfVclVci_Type())
pdnAtmBridgeIwfVclVci.setMaxAccess(_H)
if mibBuilder.loadTexts:pdnAtmBridgeIwfVclVci.setStatus(_A)
_PdnAtmBridgeIwfRowStatus_Type=RowStatus
_PdnAtmBridgeIwfRowStatus_Object=MibTableColumn
pdnAtmBridgeIwfRowStatus=_PdnAtmBridgeIwfRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,43,1,1,1,3),_PdnAtmBridgeIwfRowStatus_Type())
pdnAtmBridgeIwfRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:pdnAtmBridgeIwfRowStatus.setStatus(_A)
class _PdnAtmBridgeIwfDot1dBasePort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PdnAtmBridgeIwfDot1dBasePort_Type.__name__=_C
_PdnAtmBridgeIwfDot1dBasePort_Object=MibTableColumn
pdnAtmBridgeIwfDot1dBasePort=_PdnAtmBridgeIwfDot1dBasePort_Object((1,3,6,1,4,1,1795,2,24,2,43,1,1,1,4),_PdnAtmBridgeIwfDot1dBasePort_Type())
pdnAtmBridgeIwfDot1dBasePort.setMaxAccess(_I)
if mibBuilder.loadTexts:pdnAtmBridgeIwfDot1dBasePort.setStatus(_A)
_PdnAtmBridgeIwfConformance_ObjectIdentity=ObjectIdentity
pdnAtmBridgeIwfConformance=_PdnAtmBridgeIwfConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,43,2))
_PdnAtmBridgeIwfCompliances_ObjectIdentity=ObjectIdentity
pdnAtmBridgeIwfCompliances=_PdnAtmBridgeIwfCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,43,2,1))
_PdnAtmBridgeIwfGroups_ObjectIdentity=ObjectIdentity
pdnAtmBridgeIwfGroups=_PdnAtmBridgeIwfGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,43,2,2))
pdnAtmBridgeIwfGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,43,2,2,1))
pdnAtmBridgeIwfGroup.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:pdnAtmBridgeIwfGroup.setStatus(_A)
pdnAtmBridgeIwfMIBCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,43,2,1,1))
pdnAtmBridgeIwfMIBCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:pdnAtmBridgeIwfMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pdnAtmBridgeIwfMIB':pdnAtmBridgeIwfMIB,'pdnAtmBridgeIwfNotifications':pdnAtmBridgeIwfNotifications,'pdnAtmBridgeIwfObjects':pdnAtmBridgeIwfObjects,'pdnAtmBridgeIwfTable':pdnAtmBridgeIwfTable,'pdnAtmBridgeIwfEntry':pdnAtmBridgeIwfEntry,_F:pdnAtmBridgeIwfVclVpi,_G:pdnAtmBridgeIwfVclVci,_J:pdnAtmBridgeIwfRowStatus,_K:pdnAtmBridgeIwfDot1dBasePort,'pdnAtmBridgeIwfConformance':pdnAtmBridgeIwfConformance,'pdnAtmBridgeIwfCompliances':pdnAtmBridgeIwfCompliances,'pdnAtmBridgeIwfMIBCompliance':pdnAtmBridgeIwfMIBCompliance,'pdnAtmBridgeIwfGroups':pdnAtmBridgeIwfGroups,_L:pdnAtmBridgeIwfGroup})