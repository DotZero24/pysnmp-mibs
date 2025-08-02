_L='qtechFlashMIBGroup'
_K='qtechBootromDeviceSize'
_J='qtechBootromDeviceName'
_I='qtechFlashDeviceFree'
_H='qtechFlashDeviceUsed'
_G='qtechFlashDeviceSize'
_F='qtechFlashDeviceName'
_E='qtechBootromDeviceIndex'
_D='qtechFlashDeviceIndex'
_C='read-only'
_B='QTECH-FLASH-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
qtechFlashMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,47))
if mibBuilder.loadTexts:qtechFlashMIB.setRevisions(('2009-10-09 00:00',))
_QtechFlashMIBObjects_ObjectIdentity=ObjectIdentity
qtechFlashMIBObjects=_QtechFlashMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,47,1))
_RujieFlashDeviceTable_Object=MibTable
rujieFlashDeviceTable=_RujieFlashDeviceTable_Object((1,3,6,1,4,1,27514,1,1,10,2,47,1,1))
if mibBuilder.loadTexts:rujieFlashDeviceTable.setStatus(_A)
_RujieFlashDeviceEntry_Object=MibTableRow
rujieFlashDeviceEntry=_RujieFlashDeviceEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,47,1,1,1))
rujieFlashDeviceEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:rujieFlashDeviceEntry.setStatus(_A)
_QtechFlashDeviceIndex_Type=Unsigned32
_QtechFlashDeviceIndex_Object=MibTableColumn
qtechFlashDeviceIndex=_QtechFlashDeviceIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,47,1,1,1,1),_QtechFlashDeviceIndex_Type())
qtechFlashDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFlashDeviceIndex.setStatus(_A)
_QtechFlashDeviceName_Type=DisplayString
_QtechFlashDeviceName_Object=MibTableColumn
qtechFlashDeviceName=_QtechFlashDeviceName_Object((1,3,6,1,4,1,27514,1,1,10,2,47,1,1,1,2),_QtechFlashDeviceName_Type())
qtechFlashDeviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFlashDeviceName.setStatus(_A)
_QtechFlashDeviceSize_Type=Unsigned32
_QtechFlashDeviceSize_Object=MibTableColumn
qtechFlashDeviceSize=_QtechFlashDeviceSize_Object((1,3,6,1,4,1,27514,1,1,10,2,47,1,1,1,3),_QtechFlashDeviceSize_Type())
qtechFlashDeviceSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFlashDeviceSize.setStatus(_A)
_QtechFlashDeviceUsed_Type=Unsigned32
_QtechFlashDeviceUsed_Object=MibTableColumn
qtechFlashDeviceUsed=_QtechFlashDeviceUsed_Object((1,3,6,1,4,1,27514,1,1,10,2,47,1,1,1,4),_QtechFlashDeviceUsed_Type())
qtechFlashDeviceUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFlashDeviceUsed.setStatus(_A)
_QtechFlashDeviceFree_Type=Unsigned32
_QtechFlashDeviceFree_Object=MibTableColumn
qtechFlashDeviceFree=_QtechFlashDeviceFree_Object((1,3,6,1,4,1,27514,1,1,10,2,47,1,1,1,5),_QtechFlashDeviceFree_Type())
qtechFlashDeviceFree.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFlashDeviceFree.setStatus(_A)
_QtechBootromDeviceTable_Object=MibTable
qtechBootromDeviceTable=_QtechBootromDeviceTable_Object((1,3,6,1,4,1,27514,1,1,10,2,47,1,2))
if mibBuilder.loadTexts:qtechBootromDeviceTable.setStatus(_A)
_QtechBootromDeviceEntry_Object=MibTableRow
qtechBootromDeviceEntry=_QtechBootromDeviceEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,47,1,2,1))
qtechBootromDeviceEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:qtechBootromDeviceEntry.setStatus(_A)
_QtechBootromDeviceIndex_Type=Unsigned32
_QtechBootromDeviceIndex_Object=MibTableColumn
qtechBootromDeviceIndex=_QtechBootromDeviceIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,47,1,2,1,1),_QtechBootromDeviceIndex_Type())
qtechBootromDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBootromDeviceIndex.setStatus(_A)
_QtechBootromDeviceName_Type=DisplayString
_QtechBootromDeviceName_Object=MibTableColumn
qtechBootromDeviceName=_QtechBootromDeviceName_Object((1,3,6,1,4,1,27514,1,1,10,2,47,1,2,1,2),_QtechBootromDeviceName_Type())
qtechBootromDeviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBootromDeviceName.setStatus(_A)
_QtechBootromDeviceSize_Type=Unsigned32
_QtechBootromDeviceSize_Object=MibTableColumn
qtechBootromDeviceSize=_QtechBootromDeviceSize_Object((1,3,6,1,4,1,27514,1,1,10,2,47,1,2,1,3),_QtechBootromDeviceSize_Type())
qtechBootromDeviceSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechBootromDeviceSize.setStatus(_A)
_QtechFlashMIBConformance_ObjectIdentity=ObjectIdentity
qtechFlashMIBConformance=_QtechFlashMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,47,2))
_QtechFlashMIBCompliances_ObjectIdentity=ObjectIdentity
qtechFlashMIBCompliances=_QtechFlashMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,47,2,1))
_QtechFlashMIBGroups_ObjectIdentity=ObjectIdentity
qtechFlashMIBGroups=_QtechFlashMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,47,2,2))
qtechFlashMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,47,2,2,1))
qtechFlashMIBGroup.setObjects(*((_B,_D),(_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:qtechFlashMIBGroup.setStatus(_A)
qtechBootromDeviceMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,47,2,2,2))
qtechBootromDeviceMIBGroup.setObjects(*((_B,_E),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:qtechBootromDeviceMIBGroup.setStatus(_A)
qtechFlashMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,47,2,1,1))
qtechFlashMIBCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:qtechFlashMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechFlashMIB':qtechFlashMIB,'qtechFlashMIBObjects':qtechFlashMIBObjects,'rujieFlashDeviceTable':rujieFlashDeviceTable,'rujieFlashDeviceEntry':rujieFlashDeviceEntry,_D:qtechFlashDeviceIndex,_F:qtechFlashDeviceName,_G:qtechFlashDeviceSize,_H:qtechFlashDeviceUsed,_I:qtechFlashDeviceFree,'qtechBootromDeviceTable':qtechBootromDeviceTable,'qtechBootromDeviceEntry':qtechBootromDeviceEntry,_E:qtechBootromDeviceIndex,_J:qtechBootromDeviceName,_K:qtechBootromDeviceSize,'qtechFlashMIBConformance':qtechFlashMIBConformance,'qtechFlashMIBCompliances':qtechFlashMIBCompliances,'qtechFlashMIBCompliance':qtechFlashMIBCompliance,'qtechFlashMIBGroups':qtechFlashMIBGroups,_L:qtechFlashMIBGroup,'qtechBootromDeviceMIBGroup':qtechBootromDeviceMIBGroup})