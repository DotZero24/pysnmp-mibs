_K='etsysMauMibExtMasterSlaveGroup'
_J='etsysMauMibExtMDIXGroup'
_I='etsysIfMauExtMasterSlaveStatus'
_H='etsysIfMauExtMDIXStatus'
_G='read-write'
_F='Integer32'
_E='ifMauIfIndex'
_D='MAU-MIB'
_C='ENTERASYS-MAU-MIB-EXT-MIB'
_B='deprecated'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
ifMauIfIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
etsysMauMibExtMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,59))
if mibBuilder.loadTexts:etsysMauMibExtMIB.setRevisions(('2011-08-15 18:12','2006-05-09 11:30','2006-02-16 19:18','2005-02-07 15:05'))
_EtsysMauMibExtObjects_ObjectIdentity=ObjectIdentity
etsysMauMibExtObjects=_EtsysMauMibExtObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,59,1))
_EtsysMauMibExtBasic_ObjectIdentity=ObjectIdentity
etsysMauMibExtBasic=_EtsysMauMibExtBasic_ObjectIdentity((1,3,6,1,4,1,5624,1,2,59,1,1))
_EtsysIfMauExtMDIXTable_Object=MibTable
etsysIfMauExtMDIXTable=_EtsysIfMauExtMDIXTable_Object((1,3,6,1,4,1,5624,1,2,59,1,1,1))
if mibBuilder.loadTexts:etsysIfMauExtMDIXTable.setStatus(_A)
_EtsysIfMauExtMDIXEntry_Object=MibTableRow
etsysIfMauExtMDIXEntry=_EtsysIfMauExtMDIXEntry_Object((1,3,6,1,4,1,5624,1,2,59,1,1,1,1))
etsysIfMauExtMDIXEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:etsysIfMauExtMDIXEntry.setStatus(_A)
class _EtsysIfMauExtMDIXStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto',1),('mdix',2),('mdi',3)))
_EtsysIfMauExtMDIXStatus_Type.__name__=_F
_EtsysIfMauExtMDIXStatus_Object=MibTableColumn
etsysIfMauExtMDIXStatus=_EtsysIfMauExtMDIXStatus_Object((1,3,6,1,4,1,5624,1,2,59,1,1,1,1,1),_EtsysIfMauExtMDIXStatus_Type())
etsysIfMauExtMDIXStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:etsysIfMauExtMDIXStatus.setStatus(_A)
_EtsysIfMauExtMasterSlaveTable_Object=MibTable
etsysIfMauExtMasterSlaveTable=_EtsysIfMauExtMasterSlaveTable_Object((1,3,6,1,4,1,5624,1,2,59,1,1,2))
if mibBuilder.loadTexts:etsysIfMauExtMasterSlaveTable.setStatus(_B)
_EtsysIfMauExtMasterSlaveEntry_Object=MibTableRow
etsysIfMauExtMasterSlaveEntry=_EtsysIfMauExtMasterSlaveEntry_Object((1,3,6,1,4,1,5624,1,2,59,1,1,2,1))
etsysIfMauExtMasterSlaveEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:etsysIfMauExtMasterSlaveEntry.setStatus(_B)
class _EtsysIfMauExtMasterSlaveStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('master',1),('slave',2)))
_EtsysIfMauExtMasterSlaveStatus_Type.__name__=_F
_EtsysIfMauExtMasterSlaveStatus_Object=MibTableColumn
etsysIfMauExtMasterSlaveStatus=_EtsysIfMauExtMasterSlaveStatus_Object((1,3,6,1,4,1,5624,1,2,59,1,1,2,1,1),_EtsysIfMauExtMasterSlaveStatus_Type())
etsysIfMauExtMasterSlaveStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:etsysIfMauExtMasterSlaveStatus.setStatus(_B)
_EtsysMauMibExtConformance_ObjectIdentity=ObjectIdentity
etsysMauMibExtConformance=_EtsysMauMibExtConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,59,2))
_EtsysMauMibExtGroups_ObjectIdentity=ObjectIdentity
etsysMauMibExtGroups=_EtsysMauMibExtGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,59,2,1))
_EtsysMauMibExtCompliances_ObjectIdentity=ObjectIdentity
etsysMauMibExtCompliances=_EtsysMauMibExtCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,59,2,2))
etsysMauMibExtMDIXGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,59,2,1,1))
etsysMauMibExtMDIXGroup.setObjects((_C,_H))
if mibBuilder.loadTexts:etsysMauMibExtMDIXGroup.setStatus(_A)
etsysMauMibExtMasterSlaveGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,59,2,1,2))
etsysMauMibExtMasterSlaveGroup.setObjects((_C,_I))
if mibBuilder.loadTexts:etsysMauMibExtMasterSlaveGroup.setStatus(_B)
etsysMauMibExtMDIXCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,59,2,2,1))
etsysMauMibExtMDIXCompliance.setObjects((_C,_J))
if mibBuilder.loadTexts:etsysMauMibExtMDIXCompliance.setStatus(_A)
etsysMauMibExtMasterSlaveCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,59,2,2,2))
etsysMauMibExtMasterSlaveCompliance.setObjects((_C,_K))
if mibBuilder.loadTexts:etsysMauMibExtMasterSlaveCompliance.setStatus(_B)
mibBuilder.exportSymbols(_C,**{'etsysMauMibExtMIB':etsysMauMibExtMIB,'etsysMauMibExtObjects':etsysMauMibExtObjects,'etsysMauMibExtBasic':etsysMauMibExtBasic,'etsysIfMauExtMDIXTable':etsysIfMauExtMDIXTable,'etsysIfMauExtMDIXEntry':etsysIfMauExtMDIXEntry,_H:etsysIfMauExtMDIXStatus,'etsysIfMauExtMasterSlaveTable':etsysIfMauExtMasterSlaveTable,'etsysIfMauExtMasterSlaveEntry':etsysIfMauExtMasterSlaveEntry,_I:etsysIfMauExtMasterSlaveStatus,'etsysMauMibExtConformance':etsysMauMibExtConformance,'etsysMauMibExtGroups':etsysMauMibExtGroups,_J:etsysMauMibExtMDIXGroup,_K:etsysMauMibExtMasterSlaveGroup,'etsysMauMibExtCompliances':etsysMauMibExtCompliances,'etsysMauMibExtMDIXCompliance':etsysMauMibExtMDIXCompliance,'etsysMauMibExtMasterSlaveCompliance':etsysMauMibExtMasterSlaveCompliance})