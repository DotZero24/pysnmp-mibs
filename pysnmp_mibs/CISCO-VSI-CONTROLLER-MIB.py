_N='cvcConfGroupExternal'
_M='cvcConfGroup'
_L='cvcConfVci'
_K='cvcConfVpi'
_J='cvcConfRowStatus'
_I='cvcConfControllerName'
_H='cvcConfControllerLocation'
_G='cvcConfControllerShelfLocation'
_F='cvcConfControllerType'
_E='cvcConfControllerID'
_D='Integer32'
_C='read-create'
_B='CISCO-VSI-CONTROLLER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoVSIControllerMIB=ModuleIdentity((1,3,6,1,4,1,9,9,141))
class CvcControllerShelfLocation(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('internal',1),('external',2)))
class CvcControllerType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('par',1),('pnni',2),('lsc',3)))
_CvcMIBObjects_ObjectIdentity=ObjectIdentity
cvcMIBObjects=_CvcMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,141,1))
_CvcConfController_ObjectIdentity=ObjectIdentity
cvcConfController=_CvcConfController_ObjectIdentity((1,3,6,1,4,1,9,9,141,1,1))
_CvcConfTable_Object=MibTable
cvcConfTable=_CvcConfTable_Object((1,3,6,1,4,1,9,9,141,1,1,1))
if mibBuilder.loadTexts:cvcConfTable.setStatus(_A)
_CvcConfEntry_Object=MibTableRow
cvcConfEntry=_CvcConfEntry_Object((1,3,6,1,4,1,9,9,141,1,1,1,1))
cvcConfEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:cvcConfEntry.setStatus(_A)
class _CvcConfControllerID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CvcConfControllerID_Type.__name__=_D
_CvcConfControllerID_Object=MibTableColumn
cvcConfControllerID=_CvcConfControllerID_Object((1,3,6,1,4,1,9,9,141,1,1,1,1,1),_CvcConfControllerID_Type())
cvcConfControllerID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cvcConfControllerID.setStatus(_A)
_CvcConfControllerType_Type=CvcControllerType
_CvcConfControllerType_Object=MibTableColumn
cvcConfControllerType=_CvcConfControllerType_Object((1,3,6,1,4,1,9,9,141,1,1,1,1,2),_CvcConfControllerType_Type())
cvcConfControllerType.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcConfControllerType.setStatus(_A)
_CvcConfControllerShelfLocation_Type=CvcControllerShelfLocation
_CvcConfControllerShelfLocation_Object=MibTableColumn
cvcConfControllerShelfLocation=_CvcConfControllerShelfLocation_Object((1,3,6,1,4,1,9,9,141,1,1,1,1,3),_CvcConfControllerShelfLocation_Type())
cvcConfControllerShelfLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcConfControllerShelfLocation.setStatus(_A)
class _CvcConfControllerLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CvcConfControllerLocation_Type.__name__=_D
_CvcConfControllerLocation_Object=MibTableColumn
cvcConfControllerLocation=_CvcConfControllerLocation_Object((1,3,6,1,4,1,9,9,141,1,1,1,1,4),_CvcConfControllerLocation_Type())
cvcConfControllerLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcConfControllerLocation.setStatus(_A)
_CvcConfControllerName_Type=DisplayString
_CvcConfControllerName_Object=MibTableColumn
cvcConfControllerName=_CvcConfControllerName_Object((1,3,6,1,4,1,9,9,141,1,1,1,1,5),_CvcConfControllerName_Type())
cvcConfControllerName.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcConfControllerName.setStatus(_A)
class _CvcConfVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_CvcConfVpi_Type.__name__=_D
_CvcConfVpi_Object=MibTableColumn
cvcConfVpi=_CvcConfVpi_Object((1,3,6,1,4,1,9,9,141,1,1,1,1,6),_CvcConfVpi_Type())
cvcConfVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcConfVpi.setStatus(_A)
class _CvcConfVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,65535))
_CvcConfVci_Type.__name__=_D
_CvcConfVci_Object=MibTableColumn
cvcConfVci=_CvcConfVci_Object((1,3,6,1,4,1,9,9,141,1,1,1,1,7),_CvcConfVci_Type())
cvcConfVci.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcConfVci.setStatus(_A)
_CvcConfRowStatus_Type=RowStatus
_CvcConfRowStatus_Object=MibTableColumn
cvcConfRowStatus=_CvcConfRowStatus_Object((1,3,6,1,4,1,9,9,141,1,1,1,1,8),_CvcConfRowStatus_Type())
cvcConfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcConfRowStatus.setStatus(_A)
_CvcMIBConformance_ObjectIdentity=ObjectIdentity
cvcMIBConformance=_CvcMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,141,3))
_CvcMIBCompliances_ObjectIdentity=ObjectIdentity
cvcMIBCompliances=_CvcMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,141,3,1))
_CvcMIBGroups_ObjectIdentity=ObjectIdentity
cvcMIBGroups=_CvcMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,141,3,2))
cvcConfGroup=ObjectGroup((1,3,6,1,4,1,9,9,141,3,2,1))
cvcConfGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:cvcConfGroup.setStatus(_A)
cvcConfGroupExternal=ObjectGroup((1,3,6,1,4,1,9,9,141,3,2,2))
cvcConfGroupExternal.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:cvcConfGroupExternal.setStatus(_A)
cvcMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,141,3,1,1))
cvcMIBCompliance.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:cvcMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CvcControllerShelfLocation':CvcControllerShelfLocation,'CvcControllerType':CvcControllerType,'ciscoVSIControllerMIB':ciscoVSIControllerMIB,'cvcMIBObjects':cvcMIBObjects,'cvcConfController':cvcConfController,'cvcConfTable':cvcConfTable,'cvcConfEntry':cvcConfEntry,_E:cvcConfControllerID,_F:cvcConfControllerType,_G:cvcConfControllerShelfLocation,_H:cvcConfControllerLocation,_I:cvcConfControllerName,_K:cvcConfVpi,_L:cvcConfVci,_J:cvcConfRowStatus,'cvcMIBConformance':cvcMIBConformance,'cvcMIBCompliances':cvcMIBCompliances,'cvcMIBCompliance':cvcMIBCompliance,'cvcMIBGroups':cvcMIBGroups,_M:cvcConfGroup,_N:cvcConfGroupExternal})