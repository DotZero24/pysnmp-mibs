_F='adGenPortInfoIndex'
_E='ADTRAN-GENPORT-MIB'
_D='read-only'
_C='adGenSlotInfoIndex'
_B='ADTRAN-GENSLOT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenPortInfoIndex,=mibBuilder.importSymbols(_E,_F)
adGenSlotInfoIndex,=mibBuilder.importSymbols(_B,_C)
adGenTa5kBulkPM,adGenTa5kBulkPMID=mibBuilder.importSymbols('ADTRAN-GENTA5K-MIB','adGenTa5kBulkPM','adGenTa5kBulkPMID')
adIdentity,adIdentityShared,adMgmt,adProducts=mibBuilder.importSymbols('ADTRAN-MIB','adIdentity','adIdentityShared','adMgmt','adProducts')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adTa5kBulkPMModuleIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,67,1,18,1))
_AdTa5kBulkPMSlotTable_Object=MibTable
adTa5kBulkPMSlotTable=_AdTa5kBulkPMSlotTable_Object((1,3,6,1,4,1,664,5,67,1,18,1))
if mibBuilder.loadTexts:adTa5kBulkPMSlotTable.setStatus(_A)
_AdTa5kBulkPMSlotEntry_Object=MibTableRow
adTa5kBulkPMSlotEntry=_AdTa5kBulkPMSlotEntry_Object((1,3,6,1,4,1,664,5,67,1,18,1,1))
adTa5kBulkPMSlotEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:adTa5kBulkPMSlotEntry.setStatus(_A)
_AdTa5kBulkPMSlotInstance_Type=Integer32
_AdTa5kBulkPMSlotInstance_Object=MibTableColumn
adTa5kBulkPMSlotInstance=_AdTa5kBulkPMSlotInstance_Object((1,3,6,1,4,1,664,5,67,1,18,1,1,1),_AdTa5kBulkPMSlotInstance_Type())
adTa5kBulkPMSlotInstance.setMaxAccess(_D)
if mibBuilder.loadTexts:adTa5kBulkPMSlotInstance.setStatus(_A)
_AdTa5kBulkPM15MinSlotInstance_Type=Integer32
_AdTa5kBulkPM15MinSlotInstance_Object=MibTableColumn
adTa5kBulkPM15MinSlotInstance=_AdTa5kBulkPM15MinSlotInstance_Object((1,3,6,1,4,1,664,5,67,1,18,1,1,2),_AdTa5kBulkPM15MinSlotInstance_Type())
adTa5kBulkPM15MinSlotInstance.setMaxAccess(_D)
if mibBuilder.loadTexts:adTa5kBulkPM15MinSlotInstance.setStatus(_A)
_AdTa5kBulkPMPortTable_Object=MibTable
adTa5kBulkPMPortTable=_AdTa5kBulkPMPortTable_Object((1,3,6,1,4,1,664,5,67,1,18,2))
if mibBuilder.loadTexts:adTa5kBulkPMPortTable.setStatus(_A)
_AdTa5kBulkPMPortEntry_Object=MibTableRow
adTa5kBulkPMPortEntry=_AdTa5kBulkPMPortEntry_Object((1,3,6,1,4,1,664,5,67,1,18,2,1))
adTa5kBulkPMPortEntry.setIndexNames((0,_B,_C),(0,_E,_F))
if mibBuilder.loadTexts:adTa5kBulkPMPortEntry.setStatus(_A)
_AdTa5kBulkPMPortInstance_Type=Integer32
_AdTa5kBulkPMPortInstance_Object=MibTableColumn
adTa5kBulkPMPortInstance=_AdTa5kBulkPMPortInstance_Object((1,3,6,1,4,1,664,5,67,1,18,2,1,1),_AdTa5kBulkPMPortInstance_Type())
adTa5kBulkPMPortInstance.setMaxAccess(_D)
if mibBuilder.loadTexts:adTa5kBulkPMPortInstance.setStatus(_A)
mibBuilder.exportSymbols('ADTRAN-TA5K-BULK-PM-MIB',**{'adTa5kBulkPMSlotTable':adTa5kBulkPMSlotTable,'adTa5kBulkPMSlotEntry':adTa5kBulkPMSlotEntry,'adTa5kBulkPMSlotInstance':adTa5kBulkPMSlotInstance,'adTa5kBulkPM15MinSlotInstance':adTa5kBulkPM15MinSlotInstance,'adTa5kBulkPMPortTable':adTa5kBulkPMPortTable,'adTa5kBulkPMPortEntry':adTa5kBulkPMPortEntry,'adTa5kBulkPMPortInstance':adTa5kBulkPMPortInstance,'adTa5kBulkPMModuleIdentity':adTa5kBulkPMModuleIdentity})