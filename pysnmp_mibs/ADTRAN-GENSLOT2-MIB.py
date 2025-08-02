_C='adGenSlotInfoIndex'
_B='ADTRAN-GENSLOT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlot,adGenSlotInfoIndex=mibBuilder.importSymbols(_B,'adGenSlot',_C)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenSlot2=ModuleIdentity((1,3,6,1,4,1,664,5,13,2,5))
_AdGenSlot2ProdTable_Object=MibTable
adGenSlot2ProdTable=_AdGenSlot2ProdTable_Object((1,3,6,1,4,1,664,5,13,2,6))
if mibBuilder.loadTexts:adGenSlot2ProdTable.setStatus(_A)
_AdGenSlot2ProdEntry_Object=MibTableRow
adGenSlot2ProdEntry=_AdGenSlot2ProdEntry_Object((1,3,6,1,4,1,664,5,13,2,6,1))
adGenSlot2ProdEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:adGenSlot2ProdEntry.setStatus(_A)
_AdGenSlotProdHwRevision_Type=DisplayString
_AdGenSlotProdHwRevision_Object=MibTableColumn
adGenSlotProdHwRevision=_AdGenSlotProdHwRevision_Object((1,3,6,1,4,1,664,5,13,2,6,1,1),_AdGenSlotProdHwRevision_Type())
adGenSlotProdHwRevision.setMaxAccess('read-only')
if mibBuilder.loadTexts:adGenSlotProdHwRevision.setStatus(_A)
mibBuilder.exportSymbols('ADTRAN-GENSLOT2-MIB',**{'adGenSlot2':adGenSlot2,'adGenSlot2ProdTable':adGenSlot2ProdTable,'adGenSlot2ProdEntry':adGenSlot2ProdEntry,'adGenSlotProdHwRevision':adGenSlotProdHwRevision})