_L='fsFlashMIBGroup'
_K='fsBootromDeviceSize'
_J='fsBootromDeviceName'
_I='fsFlashDeviceFree'
_H='fsFlashDeviceUsed'
_G='fsFlashDeviceSize'
_F='fsFlashDeviceName'
_E='fsBootromDeviceIndex'
_D='fsFlashDeviceIndex'
_C='read-only'
_B='FS-FLASH-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fsFlashMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,47))
if mibBuilder.loadTexts:fsFlashMIB.setRevisions(('2009-10-09 00:00',))
_FsFlashMIBObjects_ObjectIdentity=ObjectIdentity
fsFlashMIBObjects=_FsFlashMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,47,1))
_FsFlashDeviceTable_Object=MibTable
fsFlashDeviceTable=_FsFlashDeviceTable_Object((1,3,6,1,4,1,52642,1,1,10,2,47,1,1))
if mibBuilder.loadTexts:fsFlashDeviceTable.setStatus(_A)
_FsFlashDeviceEntry_Object=MibTableRow
fsFlashDeviceEntry=_FsFlashDeviceEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,47,1,1,1))
fsFlashDeviceEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:fsFlashDeviceEntry.setStatus(_A)
_FsFlashDeviceIndex_Type=Unsigned32
_FsFlashDeviceIndex_Object=MibTableColumn
fsFlashDeviceIndex=_FsFlashDeviceIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,47,1,1,1,1),_FsFlashDeviceIndex_Type())
fsFlashDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFlashDeviceIndex.setStatus(_A)
_FsFlashDeviceName_Type=DisplayString
_FsFlashDeviceName_Object=MibTableColumn
fsFlashDeviceName=_FsFlashDeviceName_Object((1,3,6,1,4,1,52642,1,1,10,2,47,1,1,1,2),_FsFlashDeviceName_Type())
fsFlashDeviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFlashDeviceName.setStatus(_A)
_FsFlashDeviceSize_Type=Unsigned32
_FsFlashDeviceSize_Object=MibTableColumn
fsFlashDeviceSize=_FsFlashDeviceSize_Object((1,3,6,1,4,1,52642,1,1,10,2,47,1,1,1,3),_FsFlashDeviceSize_Type())
fsFlashDeviceSize.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFlashDeviceSize.setStatus(_A)
_FsFlashDeviceUsed_Type=Unsigned32
_FsFlashDeviceUsed_Object=MibTableColumn
fsFlashDeviceUsed=_FsFlashDeviceUsed_Object((1,3,6,1,4,1,52642,1,1,10,2,47,1,1,1,4),_FsFlashDeviceUsed_Type())
fsFlashDeviceUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFlashDeviceUsed.setStatus(_A)
_FsFlashDeviceFree_Type=Unsigned32
_FsFlashDeviceFree_Object=MibTableColumn
fsFlashDeviceFree=_FsFlashDeviceFree_Object((1,3,6,1,4,1,52642,1,1,10,2,47,1,1,1,5),_FsFlashDeviceFree_Type())
fsFlashDeviceFree.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFlashDeviceFree.setStatus(_A)
_FsBootromDeviceTable_Object=MibTable
fsBootromDeviceTable=_FsBootromDeviceTable_Object((1,3,6,1,4,1,52642,1,1,10,2,47,1,2))
if mibBuilder.loadTexts:fsBootromDeviceTable.setStatus(_A)
_FsBootromDeviceEntry_Object=MibTableRow
fsBootromDeviceEntry=_FsBootromDeviceEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,47,1,2,1))
fsBootromDeviceEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:fsBootromDeviceEntry.setStatus(_A)
_FsBootromDeviceIndex_Type=Unsigned32
_FsBootromDeviceIndex_Object=MibTableColumn
fsBootromDeviceIndex=_FsBootromDeviceIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,47,1,2,1,1),_FsBootromDeviceIndex_Type())
fsBootromDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBootromDeviceIndex.setStatus(_A)
_FsBootromDeviceName_Type=DisplayString
_FsBootromDeviceName_Object=MibTableColumn
fsBootromDeviceName=_FsBootromDeviceName_Object((1,3,6,1,4,1,52642,1,1,10,2,47,1,2,1,2),_FsBootromDeviceName_Type())
fsBootromDeviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBootromDeviceName.setStatus(_A)
_FsBootromDeviceSize_Type=Unsigned32
_FsBootromDeviceSize_Object=MibTableColumn
fsBootromDeviceSize=_FsBootromDeviceSize_Object((1,3,6,1,4,1,52642,1,1,10,2,47,1,2,1,3),_FsBootromDeviceSize_Type())
fsBootromDeviceSize.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBootromDeviceSize.setStatus(_A)
_FsFlashMIBConformance_ObjectIdentity=ObjectIdentity
fsFlashMIBConformance=_FsFlashMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,47,2))
_FsFlashMIBCompliances_ObjectIdentity=ObjectIdentity
fsFlashMIBCompliances=_FsFlashMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,47,2,1))
_FsFlashMIBGroups_ObjectIdentity=ObjectIdentity
fsFlashMIBGroups=_FsFlashMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,47,2,2))
fsFlashMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,47,2,2,1))
fsFlashMIBGroup.setObjects(*((_B,_D),(_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:fsFlashMIBGroup.setStatus(_A)
fsBootromDeviceMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,47,2,2,2))
fsBootromDeviceMIBGroup.setObjects(*((_B,_E),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:fsBootromDeviceMIBGroup.setStatus(_A)
fsFlashMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,47,2,1,1))
fsFlashMIBCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:fsFlashMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsFlashMIB':fsFlashMIB,'fsFlashMIBObjects':fsFlashMIBObjects,'fsFlashDeviceTable':fsFlashDeviceTable,'fsFlashDeviceEntry':fsFlashDeviceEntry,_D:fsFlashDeviceIndex,_F:fsFlashDeviceName,_G:fsFlashDeviceSize,_H:fsFlashDeviceUsed,_I:fsFlashDeviceFree,'fsBootromDeviceTable':fsBootromDeviceTable,'fsBootromDeviceEntry':fsBootromDeviceEntry,_E:fsBootromDeviceIndex,_J:fsBootromDeviceName,_K:fsBootromDeviceSize,'fsFlashMIBConformance':fsFlashMIBConformance,'fsFlashMIBCompliances':fsFlashMIBCompliances,'fsFlashMIBCompliance':fsFlashMIBCompliance,'fsFlashMIBGroups':fsFlashMIBGroups,_L:fsFlashMIBGroup,'fsBootromDeviceMIBGroup':fsBootromDeviceMIBGroup})