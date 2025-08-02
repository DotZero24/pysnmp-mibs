_L='pdnIfDevIwfStatsTotalRxGroup'
_K='pdnIfDevIwfStatsTotalMRUErrorsGroup'
_J='pdnIfDevIwfStatsTotalBufferUnderrunsGroup'
_I='pdnIfDevIwfStatsTotalRx'
_H='pdnIfDevIwfStatsTotalRxUnit'
_G='pdnIfDevIwfStatsTotalMRUErrors'
_F='pdnIfDevIwfStatsTotalBufferUnderruns'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='PDN-IFDEV-IWF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
pdn_interfaces,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-interfaces')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pdnIfDevIwfMIB=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,6,27))
if mibBuilder.loadTexts:pdnIfDevIwfMIB.setRevisions(('2004-09-10 00:00',))
class TxRxUnit(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('bits',2),('octets',3),('frames',4),('packets',5),('datagrams',6)))
_PdnIfDevIwfNotifications_ObjectIdentity=ObjectIdentity
pdnIfDevIwfNotifications=_PdnIfDevIwfNotifications_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,27,0))
_PdnIfDevIwfObjects_ObjectIdentity=ObjectIdentity
pdnIfDevIwfObjects=_PdnIfDevIwfObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,27,1))
_PdnIfDevIwfStatsTotalTable_Object=MibTable
pdnIfDevIwfStatsTotalTable=_PdnIfDevIwfStatsTotalTable_Object((1,3,6,1,4,1,1795,2,24,2,6,27,1,1))
if mibBuilder.loadTexts:pdnIfDevIwfStatsTotalTable.setStatus(_A)
_PdnIfDevIwfStatsTotalEntry_Object=MibTableRow
pdnIfDevIwfStatsTotalEntry=_PdnIfDevIwfStatsTotalEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,27,1,1,1))
pdnIfDevIwfStatsTotalEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:pdnIfDevIwfStatsTotalEntry.setStatus(_A)
_PdnIfDevIwfStatsTotalBufferUnderruns_Type=Counter32
_PdnIfDevIwfStatsTotalBufferUnderruns_Object=MibTableColumn
pdnIfDevIwfStatsTotalBufferUnderruns=_PdnIfDevIwfStatsTotalBufferUnderruns_Object((1,3,6,1,4,1,1795,2,24,2,6,27,1,1,1,1),_PdnIfDevIwfStatsTotalBufferUnderruns_Type())
pdnIfDevIwfStatsTotalBufferUnderruns.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnIfDevIwfStatsTotalBufferUnderruns.setStatus(_A)
_PdnIfDevIwfStatsTotalMRUErrors_Type=Counter32
_PdnIfDevIwfStatsTotalMRUErrors_Object=MibTableColumn
pdnIfDevIwfStatsTotalMRUErrors=_PdnIfDevIwfStatsTotalMRUErrors_Object((1,3,6,1,4,1,1795,2,24,2,6,27,1,1,1,2),_PdnIfDevIwfStatsTotalMRUErrors_Type())
pdnIfDevIwfStatsTotalMRUErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnIfDevIwfStatsTotalMRUErrors.setStatus(_A)
_PdnIfDevIwfStatsTotalRxUnit_Type=TxRxUnit
_PdnIfDevIwfStatsTotalRxUnit_Object=MibTableColumn
pdnIfDevIwfStatsTotalRxUnit=_PdnIfDevIwfStatsTotalRxUnit_Object((1,3,6,1,4,1,1795,2,24,2,6,27,1,1,1,3),_PdnIfDevIwfStatsTotalRxUnit_Type())
pdnIfDevIwfStatsTotalRxUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnIfDevIwfStatsTotalRxUnit.setStatus(_A)
_PdnIfDevIwfStatsTotalRx_Type=Counter32
_PdnIfDevIwfStatsTotalRx_Object=MibTableColumn
pdnIfDevIwfStatsTotalRx=_PdnIfDevIwfStatsTotalRx_Object((1,3,6,1,4,1,1795,2,24,2,6,27,1,1,1,4),_PdnIfDevIwfStatsTotalRx_Type())
pdnIfDevIwfStatsTotalRx.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnIfDevIwfStatsTotalRx.setStatus(_A)
_PdnIfDevIwfAFNs_ObjectIdentity=ObjectIdentity
pdnIfDevIwfAFNs=_PdnIfDevIwfAFNs_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,27,2))
_PdnIfDevIwfConformance_ObjectIdentity=ObjectIdentity
pdnIfDevIwfConformance=_PdnIfDevIwfConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,27,3))
_PdnIfDevIwfCompliances_ObjectIdentity=ObjectIdentity
pdnIfDevIwfCompliances=_PdnIfDevIwfCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,27,3,1))
_PdnIfDevIwfGroups_ObjectIdentity=ObjectIdentity
pdnIfDevIwfGroups=_PdnIfDevIwfGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,27,3,2))
_PdnIfDevIwfObjGroups_ObjectIdentity=ObjectIdentity
pdnIfDevIwfObjGroups=_PdnIfDevIwfObjGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,27,3,2,1))
_PdnIfDevIwfAfnGroups_ObjectIdentity=ObjectIdentity
pdnIfDevIwfAfnGroups=_PdnIfDevIwfAfnGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,27,3,2,2))
_PdnIfDevIwfNtfyGroups_ObjectIdentity=ObjectIdentity
pdnIfDevIwfNtfyGroups=_PdnIfDevIwfNtfyGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,27,3,2,3))
pdnIfDevIwfStatsTotalBufferUnderrunsGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,27,3,2,1,1))
pdnIfDevIwfStatsTotalBufferUnderrunsGroup.setObjects((_B,_F))
if mibBuilder.loadTexts:pdnIfDevIwfStatsTotalBufferUnderrunsGroup.setStatus(_A)
pdnIfDevIwfStatsTotalMRUErrorsGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,27,3,2,1,2))
pdnIfDevIwfStatsTotalMRUErrorsGroup.setObjects((_B,_G))
if mibBuilder.loadTexts:pdnIfDevIwfStatsTotalMRUErrorsGroup.setStatus(_A)
pdnIfDevIwfStatsTotalRxGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,27,3,2,1,3))
pdnIfDevIwfStatsTotalRxGroup.setObjects(*((_B,_H),(_B,_I)))
if mibBuilder.loadTexts:pdnIfDevIwfStatsTotalRxGroup.setStatus(_A)
pdnIfDevIwfCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,6,27,3,1,1))
pdnIfDevIwfCompliance.setObjects(*((_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:pdnIfDevIwfCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TxRxUnit':TxRxUnit,'pdnIfDevIwfMIB':pdnIfDevIwfMIB,'pdnIfDevIwfNotifications':pdnIfDevIwfNotifications,'pdnIfDevIwfObjects':pdnIfDevIwfObjects,'pdnIfDevIwfStatsTotalTable':pdnIfDevIwfStatsTotalTable,'pdnIfDevIwfStatsTotalEntry':pdnIfDevIwfStatsTotalEntry,_F:pdnIfDevIwfStatsTotalBufferUnderruns,_G:pdnIfDevIwfStatsTotalMRUErrors,_H:pdnIfDevIwfStatsTotalRxUnit,_I:pdnIfDevIwfStatsTotalRx,'pdnIfDevIwfAFNs':pdnIfDevIwfAFNs,'pdnIfDevIwfConformance':pdnIfDevIwfConformance,'pdnIfDevIwfCompliances':pdnIfDevIwfCompliances,'pdnIfDevIwfCompliance':pdnIfDevIwfCompliance,'pdnIfDevIwfGroups':pdnIfDevIwfGroups,'pdnIfDevIwfObjGroups':pdnIfDevIwfObjGroups,_J:pdnIfDevIwfStatsTotalBufferUnderrunsGroup,_K:pdnIfDevIwfStatsTotalMRUErrorsGroup,_L:pdnIfDevIwfStatsTotalRxGroup,'pdnIfDevIwfAfnGroups':pdnIfDevIwfAfnGroups,'pdnIfDevIwfNtfyGroups':pdnIfDevIwfNtfyGroups})