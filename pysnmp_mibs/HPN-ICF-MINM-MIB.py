_K='hpnicfMinmConnectionLinkId'
_J='HPN-ICF-MINM-MIB'
_I='read-write'
_H='ifIndex'
_G='IF-MIB'
_F='read-only'
_E='hpnicfVsiIndex'
_D='HPN-ICF-VSI-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
hpnicfVsiIndex,=mibBuilder.importSymbols(_D,_E)
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
hpnicfMinm=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,107))
if mibBuilder.loadTexts:hpnicfMinm.setRevisions(('2009-08-08 10:00',))
class HpnicfMinmEnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_HpnicfMinmObjects_ObjectIdentity=ObjectIdentity
hpnicfMinmObjects=_HpnicfMinmObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,107,1))
_HpnicfMinmScalarGroup_ObjectIdentity=ObjectIdentity
hpnicfMinmScalarGroup=_HpnicfMinmScalarGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,107,1,1))
class _HpnicfMinmCapabilities_Type(Bits):namedValues=NamedValues(*(('reEncapsulation',0),('uplink',1),('vsiShareConnection',2)))
_HpnicfMinmCapabilities_Type.__name__='Bits'
_HpnicfMinmCapabilities_Object=MibScalar
hpnicfMinmCapabilities=_HpnicfMinmCapabilities_Object((1,3,6,1,4,1,11,2,14,11,15,2,107,1,1,1),_HpnicfMinmCapabilities_Type())
hpnicfMinmCapabilities.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMinmCapabilities.setStatus(_A)
_HpnicfMinmBmac_Type=MacAddress
_HpnicfMinmBmac_Object=MibScalar
hpnicfMinmBmac=_HpnicfMinmBmac_Object((1,3,6,1,4,1,11,2,14,11,15,2,107,1,1,2),_HpnicfMinmBmac_Type())
hpnicfMinmBmac.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMinmBmac.setStatus(_A)
_HpnicfMinmVsiTable_Object=MibTable
hpnicfMinmVsiTable=_HpnicfMinmVsiTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,107,1,2))
if mibBuilder.loadTexts:hpnicfMinmVsiTable.setStatus(_A)
_HpnicfMinmVsiEntry_Object=MibTableRow
hpnicfMinmVsiEntry=_HpnicfMinmVsiEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,107,1,2,1))
hpnicfMinmVsiEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpnicfMinmVsiEntry.setStatus(_A)
class _HpnicfMinmVsiBvlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094),ValueRangeConstraint(65535,65535))
_HpnicfMinmVsiBvlan_Type.__name__=_C
_HpnicfMinmVsiBvlan_Object=MibTableColumn
hpnicfMinmVsiBvlan=_HpnicfMinmVsiBvlan_Object((1,3,6,1,4,1,11,2,14,11,15,2,107,1,2,1,1),_HpnicfMinmVsiBvlan_Type())
hpnicfMinmVsiBvlan.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfMinmVsiBvlan.setStatus(_A)
_HpnicfMinmVsiReEncapsulation_Type=HpnicfMinmEnabledStatus
_HpnicfMinmVsiReEncapsulation_Object=MibTableColumn
hpnicfMinmVsiReEncapsulation=_HpnicfMinmVsiReEncapsulation_Object((1,3,6,1,4,1,11,2,14,11,15,2,107,1,2,1,2),_HpnicfMinmVsiReEncapsulation_Type())
hpnicfMinmVsiReEncapsulation.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfMinmVsiReEncapsulation.setStatus(_A)
_HpnicfMinmVsiNextAvailableLinkId_Type=Unsigned32
_HpnicfMinmVsiNextAvailableLinkId_Object=MibTableColumn
hpnicfMinmVsiNextAvailableLinkId=_HpnicfMinmVsiNextAvailableLinkId_Object((1,3,6,1,4,1,11,2,14,11,15,2,107,1,2,1,3),_HpnicfMinmVsiNextAvailableLinkId_Type())
hpnicfMinmVsiNextAvailableLinkId.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMinmVsiNextAvailableLinkId.setStatus(_A)
_HpnicfMinmUplinkTable_Object=MibTable
hpnicfMinmUplinkTable=_HpnicfMinmUplinkTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,107,1,3))
if mibBuilder.loadTexts:hpnicfMinmUplinkTable.setStatus(_A)
_HpnicfMinmUplinkEntry_Object=MibTableRow
hpnicfMinmUplinkEntry=_HpnicfMinmUplinkEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,107,1,3,1))
hpnicfMinmUplinkEntry.setIndexNames((0,_D,_E),(0,_G,_H))
if mibBuilder.loadTexts:hpnicfMinmUplinkEntry.setStatus(_A)
_HpnicfMinmUplinkRowStatus_Type=RowStatus
_HpnicfMinmUplinkRowStatus_Object=MibTableColumn
hpnicfMinmUplinkRowStatus=_HpnicfMinmUplinkRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,107,1,3,1,1),_HpnicfMinmUplinkRowStatus_Type())
hpnicfMinmUplinkRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMinmUplinkRowStatus.setStatus(_A)
_HpnicfMinmConnectionTable_Object=MibTable
hpnicfMinmConnectionTable=_HpnicfMinmConnectionTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,107,1,4))
if mibBuilder.loadTexts:hpnicfMinmConnectionTable.setStatus(_A)
_HpnicfMinmConnectionEntry_Object=MibTableRow
hpnicfMinmConnectionEntry=_HpnicfMinmConnectionEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,107,1,4,1))
hpnicfMinmConnectionEntry.setIndexNames((0,_D,_E),(0,_J,_K))
if mibBuilder.loadTexts:hpnicfMinmConnectionEntry.setStatus(_A)
_HpnicfMinmConnectionLinkId_Type=Unsigned32
_HpnicfMinmConnectionLinkId_Object=MibTableColumn
hpnicfMinmConnectionLinkId=_HpnicfMinmConnectionLinkId_Object((1,3,6,1,4,1,11,2,14,11,15,2,107,1,4,1,1),_HpnicfMinmConnectionLinkId_Type())
hpnicfMinmConnectionLinkId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpnicfMinmConnectionLinkId.setStatus(_A)
_HpnicfMinmConnectionBmac_Type=MacAddress
_HpnicfMinmConnectionBmac_Object=MibTableColumn
hpnicfMinmConnectionBmac=_HpnicfMinmConnectionBmac_Object((1,3,6,1,4,1,11,2,14,11,15,2,107,1,4,1,2),_HpnicfMinmConnectionBmac_Type())
hpnicfMinmConnectionBmac.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMinmConnectionBmac.setStatus(_A)
class _HpnicfMinmConnectionBvlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HpnicfMinmConnectionBvlan_Type.__name__=_C
_HpnicfMinmConnectionBvlan_Object=MibTableColumn
hpnicfMinmConnectionBvlan=_HpnicfMinmConnectionBvlan_Object((1,3,6,1,4,1,11,2,14,11,15,2,107,1,4,1,3),_HpnicfMinmConnectionBvlan_Type())
hpnicfMinmConnectionBvlan.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMinmConnectionBvlan.setStatus(_A)
_HpnicfMinmConnectionPort_Type=Integer32
_HpnicfMinmConnectionPort_Object=MibTableColumn
hpnicfMinmConnectionPort=_HpnicfMinmConnectionPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,107,1,4,1,4),_HpnicfMinmConnectionPort_Type())
hpnicfMinmConnectionPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMinmConnectionPort.setStatus(_A)
class _HpnicfMinmConnectionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('learned',1),('configDynamic',2),('configStatic',3),('blackhole',4)))
_HpnicfMinmConnectionStatus_Type.__name__=_C
_HpnicfMinmConnectionStatus_Object=MibTableColumn
hpnicfMinmConnectionStatus=_HpnicfMinmConnectionStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,107,1,4,1,5),_HpnicfMinmConnectionStatus_Type())
hpnicfMinmConnectionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMinmConnectionStatus.setStatus(_A)
class _HpnicfMinmConnectionAgingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('aging',1),('noAged',2)))
_HpnicfMinmConnectionAgingStatus_Type.__name__=_C
_HpnicfMinmConnectionAgingStatus_Object=MibTableColumn
hpnicfMinmConnectionAgingStatus=_HpnicfMinmConnectionAgingStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,107,1,4,1,6),_HpnicfMinmConnectionAgingStatus_Type())
hpnicfMinmConnectionAgingStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMinmConnectionAgingStatus.setStatus(_A)
_HpnicfMinmConnectionRowStatus_Type=RowStatus
_HpnicfMinmConnectionRowStatus_Object=MibTableColumn
hpnicfMinmConnectionRowStatus=_HpnicfMinmConnectionRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,107,1,4,1,7),_HpnicfMinmConnectionRowStatus_Type())
hpnicfMinmConnectionRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMinmConnectionRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_J,**{'HpnicfMinmEnabledStatus':HpnicfMinmEnabledStatus,'hpnicfMinm':hpnicfMinm,'hpnicfMinmObjects':hpnicfMinmObjects,'hpnicfMinmScalarGroup':hpnicfMinmScalarGroup,'hpnicfMinmCapabilities':hpnicfMinmCapabilities,'hpnicfMinmBmac':hpnicfMinmBmac,'hpnicfMinmVsiTable':hpnicfMinmVsiTable,'hpnicfMinmVsiEntry':hpnicfMinmVsiEntry,'hpnicfMinmVsiBvlan':hpnicfMinmVsiBvlan,'hpnicfMinmVsiReEncapsulation':hpnicfMinmVsiReEncapsulation,'hpnicfMinmVsiNextAvailableLinkId':hpnicfMinmVsiNextAvailableLinkId,'hpnicfMinmUplinkTable':hpnicfMinmUplinkTable,'hpnicfMinmUplinkEntry':hpnicfMinmUplinkEntry,'hpnicfMinmUplinkRowStatus':hpnicfMinmUplinkRowStatus,'hpnicfMinmConnectionTable':hpnicfMinmConnectionTable,'hpnicfMinmConnectionEntry':hpnicfMinmConnectionEntry,_K:hpnicfMinmConnectionLinkId,'hpnicfMinmConnectionBmac':hpnicfMinmConnectionBmac,'hpnicfMinmConnectionBvlan':hpnicfMinmConnectionBvlan,'hpnicfMinmConnectionPort':hpnicfMinmConnectionPort,'hpnicfMinmConnectionStatus':hpnicfMinmConnectionStatus,'hpnicfMinmConnectionAgingStatus':hpnicfMinmConnectionAgingStatus,'hpnicfMinmConnectionRowStatus':hpnicfMinmConnectionRowStatus})