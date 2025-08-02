_K='adTa5kTlvBySlotSequence'
_J='read-only'
_I='adTa5kTlvSequence'
_H='adTa5kTlvBySlotInstance'
_G='adTa5kTlvInstance'
_F='adGenSlotInfoIndex'
_E='ADTRAN-GENSLOT-MIB'
_D='not-accessible'
_C='read-write'
_B='ADTRAN-TA5K-TLV-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenPortInfoIndex,=mibBuilder.importSymbols('ADTRAN-GENPORT-MIB','adGenPortInfoIndex')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_E,_F)
adGenTa5kTlv,adGenTa5kTlvID=mibBuilder.importSymbols('ADTRAN-GENTA5K-MIB','adGenTa5kTlv','adGenTa5kTlvID')
adIdentity,adIdentityShared,adMgmt,adProducts=mibBuilder.importSymbols('ADTRAN-MIB','adIdentity','adIdentityShared','adMgmt','adProducts')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adTa5kTlvModuleIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,67,1,5,1))
if mibBuilder.loadTexts:adTa5kTlvModuleIdentity.setRevisions(('2012-09-18 00:00',))
_AdTa5kTlvCountTable_Object=MibTable
adTa5kTlvCountTable=_AdTa5kTlvCountTable_Object((1,3,6,1,4,1,664,5,67,1,5,1))
if mibBuilder.loadTexts:adTa5kTlvCountTable.setStatus(_A)
_AdTa5kTlvCountEntry_Object=MibTableRow
adTa5kTlvCountEntry=_AdTa5kTlvCountEntry_Object((1,3,6,1,4,1,664,5,67,1,5,1,1))
adTa5kTlvCountEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:adTa5kTlvCountEntry.setStatus(_A)
_AdTa5kTlvCount_Type=Integer32
_AdTa5kTlvCount_Object=MibTableColumn
adTa5kTlvCount=_AdTa5kTlvCount_Object((1,3,6,1,4,1,664,5,67,1,5,1,1,1),_AdTa5kTlvCount_Type())
adTa5kTlvCount.setMaxAccess(_C)
if mibBuilder.loadTexts:adTa5kTlvCount.setStatus(_A)
_AdTa5kTlvInstance_Type=Integer32
_AdTa5kTlvInstance_Object=MibTableColumn
adTa5kTlvInstance=_AdTa5kTlvInstance_Object((1,3,6,1,4,1,664,5,67,1,5,1,1,2),_AdTa5kTlvInstance_Type())
adTa5kTlvInstance.setMaxAccess(_D)
if mibBuilder.loadTexts:adTa5kTlvInstance.setStatus(_A)
_AdTa5kTlvDelete_Type=Integer32
_AdTa5kTlvDelete_Object=MibTableColumn
adTa5kTlvDelete=_AdTa5kTlvDelete_Object((1,3,6,1,4,1,664,5,67,1,5,1,1,3),_AdTa5kTlvDelete_Type())
adTa5kTlvDelete.setMaxAccess(_C)
if mibBuilder.loadTexts:adTa5kTlvDelete.setStatus(_A)
_AdTa5kTlvTable_Object=MibTable
adTa5kTlvTable=_AdTa5kTlvTable_Object((1,3,6,1,4,1,664,5,67,1,5,2))
if mibBuilder.loadTexts:adTa5kTlvTable.setStatus(_A)
_AdTa5kTlvEntry_Object=MibTableRow
adTa5kTlvEntry=_AdTa5kTlvEntry_Object((1,3,6,1,4,1,664,5,67,1,5,2,1))
adTa5kTlvEntry.setIndexNames((0,_B,_G),(0,_B,_I))
if mibBuilder.loadTexts:adTa5kTlvEntry.setStatus(_A)
_AdTa5kTlvBulk_Type=OctetString
_AdTa5kTlvBulk_Object=MibTableColumn
adTa5kTlvBulk=_AdTa5kTlvBulk_Object((1,3,6,1,4,1,664,5,67,1,5,2,1,1),_AdTa5kTlvBulk_Type())
adTa5kTlvBulk.setMaxAccess(_J)
if mibBuilder.loadTexts:adTa5kTlvBulk.setStatus(_A)
_AdTa5kTlvSequence_Type=Integer32
_AdTa5kTlvSequence_Object=MibTableColumn
adTa5kTlvSequence=_AdTa5kTlvSequence_Object((1,3,6,1,4,1,664,5,67,1,5,2,1,2),_AdTa5kTlvSequence_Type())
adTa5kTlvSequence.setMaxAccess(_D)
if mibBuilder.loadTexts:adTa5kTlvSequence.setStatus(_A)
_AdTa5kTlvBySlotCountTable_Object=MibTable
adTa5kTlvBySlotCountTable=_AdTa5kTlvBySlotCountTable_Object((1,3,6,1,4,1,664,5,67,1,5,3))
if mibBuilder.loadTexts:adTa5kTlvBySlotCountTable.setStatus(_A)
_AdTa5kTlvBySlotCountEntry_Object=MibTableRow
adTa5kTlvBySlotCountEntry=_AdTa5kTlvBySlotCountEntry_Object((1,3,6,1,4,1,664,5,67,1,5,3,1))
adTa5kTlvBySlotCountEntry.setIndexNames((0,_E,_F),(0,_B,_H))
if mibBuilder.loadTexts:adTa5kTlvBySlotCountEntry.setStatus(_A)
_AdTa5kTlvBySlotCount_Type=Integer32
_AdTa5kTlvBySlotCount_Object=MibTableColumn
adTa5kTlvBySlotCount=_AdTa5kTlvBySlotCount_Object((1,3,6,1,4,1,664,5,67,1,5,3,1,1),_AdTa5kTlvBySlotCount_Type())
adTa5kTlvBySlotCount.setMaxAccess(_C)
if mibBuilder.loadTexts:adTa5kTlvBySlotCount.setStatus(_A)
_AdTa5kTlvBySlotInstance_Type=Integer32
_AdTa5kTlvBySlotInstance_Object=MibTableColumn
adTa5kTlvBySlotInstance=_AdTa5kTlvBySlotInstance_Object((1,3,6,1,4,1,664,5,67,1,5,3,1,2),_AdTa5kTlvBySlotInstance_Type())
adTa5kTlvBySlotInstance.setMaxAccess(_D)
if mibBuilder.loadTexts:adTa5kTlvBySlotInstance.setStatus(_A)
_AdTa5kTlvBySlotDelete_Type=Integer32
_AdTa5kTlvBySlotDelete_Object=MibTableColumn
adTa5kTlvBySlotDelete=_AdTa5kTlvBySlotDelete_Object((1,3,6,1,4,1,664,5,67,1,5,3,1,3),_AdTa5kTlvBySlotDelete_Type())
adTa5kTlvBySlotDelete.setMaxAccess(_C)
if mibBuilder.loadTexts:adTa5kTlvBySlotDelete.setStatus(_A)
_AdTa5kTlvBySlotTable_Object=MibTable
adTa5kTlvBySlotTable=_AdTa5kTlvBySlotTable_Object((1,3,6,1,4,1,664,5,67,1,5,4))
if mibBuilder.loadTexts:adTa5kTlvBySlotTable.setStatus(_A)
_AdTa5kTlvBySlotEntry_Object=MibTableRow
adTa5kTlvBySlotEntry=_AdTa5kTlvBySlotEntry_Object((1,3,6,1,4,1,664,5,67,1,5,4,1))
adTa5kTlvBySlotEntry.setIndexNames((0,_E,_F),(0,_B,_H),(0,_B,_K))
if mibBuilder.loadTexts:adTa5kTlvBySlotEntry.setStatus(_A)
_AdTa5kTlvBySlotBulk_Type=OctetString
_AdTa5kTlvBySlotBulk_Object=MibTableColumn
adTa5kTlvBySlotBulk=_AdTa5kTlvBySlotBulk_Object((1,3,6,1,4,1,664,5,67,1,5,4,1,1),_AdTa5kTlvBySlotBulk_Type())
adTa5kTlvBySlotBulk.setMaxAccess(_J)
if mibBuilder.loadTexts:adTa5kTlvBySlotBulk.setStatus(_A)
_AdTa5kTlvBySlotSequence_Type=Integer32
_AdTa5kTlvBySlotSequence_Object=MibTableColumn
adTa5kTlvBySlotSequence=_AdTa5kTlvBySlotSequence_Object((1,3,6,1,4,1,664,5,67,1,5,4,1,2),_AdTa5kTlvBySlotSequence_Type())
adTa5kTlvBySlotSequence.setMaxAccess(_D)
if mibBuilder.loadTexts:adTa5kTlvBySlotSequence.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'adTa5kTlvCountTable':adTa5kTlvCountTable,'adTa5kTlvCountEntry':adTa5kTlvCountEntry,'adTa5kTlvCount':adTa5kTlvCount,_G:adTa5kTlvInstance,'adTa5kTlvDelete':adTa5kTlvDelete,'adTa5kTlvTable':adTa5kTlvTable,'adTa5kTlvEntry':adTa5kTlvEntry,'adTa5kTlvBulk':adTa5kTlvBulk,_I:adTa5kTlvSequence,'adTa5kTlvBySlotCountTable':adTa5kTlvBySlotCountTable,'adTa5kTlvBySlotCountEntry':adTa5kTlvBySlotCountEntry,'adTa5kTlvBySlotCount':adTa5kTlvBySlotCount,_H:adTa5kTlvBySlotInstance,'adTa5kTlvBySlotDelete':adTa5kTlvBySlotDelete,'adTa5kTlvBySlotTable':adTa5kTlvBySlotTable,'adTa5kTlvBySlotEntry':adTa5kTlvBySlotEntry,'adTa5kTlvBySlotBulk':adTa5kTlvBySlotBulk,_K:adTa5kTlvBySlotSequence,'adTa5kTlvModuleIdentity':adTa5kTlvModuleIdentity})