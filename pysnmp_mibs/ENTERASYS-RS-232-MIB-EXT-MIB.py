_L='etsysRs232MibExtCtsLinkGroup'
_K='etsysRs232MibExtVt100DsrGroup'
_J='etsysRs232CtsLinkEnableState'
_I='etsysRs232Vt100DsrTimeout'
_H='etsysRs232Vt100DsrEnableState'
_G='etsysRs232CtsLinkExtEntry'
_F='etsysRs232Vt100ExtEntry'
_E='Integer32'
_D='read-write'
_C='EnabledStatus'
_B='ENTERASYS-RS-232-MIB-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_C)
rs232PortEntry,=mibBuilder.importSymbols('RS-232-MIB','rs232PortEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
etsysRs232MibExtMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,77))
if mibBuilder.loadTexts:etsysRs232MibExtMIB.setRevisions(('2011-06-22 14:50','2010-11-09 20:07'))
_EtsysRs232MibExtObjects_ObjectIdentity=ObjectIdentity
etsysRs232MibExtObjects=_EtsysRs232MibExtObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,77,1))
_EtsysRs232MibExtVt100_ObjectIdentity=ObjectIdentity
etsysRs232MibExtVt100=_EtsysRs232MibExtVt100_ObjectIdentity((1,3,6,1,4,1,5624,1,2,77,1,1))
_EtsysRs232Vt100ExtTable_Object=MibTable
etsysRs232Vt100ExtTable=_EtsysRs232Vt100ExtTable_Object((1,3,6,1,4,1,5624,1,2,77,1,1,1))
if mibBuilder.loadTexts:etsysRs232Vt100ExtTable.setStatus(_A)
_EtsysRs232Vt100ExtEntry_Object=MibTableRow
etsysRs232Vt100ExtEntry=_EtsysRs232Vt100ExtEntry_Object((1,3,6,1,4,1,5624,1,2,77,1,1,1,1))
if mibBuilder.loadTexts:etsysRs232Vt100ExtEntry.setStatus(_A)
class _EtsysRs232Vt100DsrEnableState_Type(EnabledStatus):defaultValue=2
_EtsysRs232Vt100DsrEnableState_Type.__name__=_C
_EtsysRs232Vt100DsrEnableState_Object=MibTableColumn
etsysRs232Vt100DsrEnableState=_EtsysRs232Vt100DsrEnableState_Object((1,3,6,1,4,1,5624,1,2,77,1,1,1,1,1),_EtsysRs232Vt100DsrEnableState_Type())
etsysRs232Vt100DsrEnableState.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysRs232Vt100DsrEnableState.setStatus(_A)
class _EtsysRs232Vt100DsrTimeout_Type(Integer32):defaultValue=3
_EtsysRs232Vt100DsrTimeout_Type.__name__=_E
_EtsysRs232Vt100DsrTimeout_Object=MibTableColumn
etsysRs232Vt100DsrTimeout=_EtsysRs232Vt100DsrTimeout_Object((1,3,6,1,4,1,5624,1,2,77,1,1,1,1,2),_EtsysRs232Vt100DsrTimeout_Type())
etsysRs232Vt100DsrTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysRs232Vt100DsrTimeout.setStatus(_A)
if mibBuilder.loadTexts:etsysRs232Vt100DsrTimeout.setUnits('seconds')
_EtsysRs232MibExtCtsLink_ObjectIdentity=ObjectIdentity
etsysRs232MibExtCtsLink=_EtsysRs232MibExtCtsLink_ObjectIdentity((1,3,6,1,4,1,5624,1,2,77,1,2))
_EtsysRs232CtsLinkExtTable_Object=MibTable
etsysRs232CtsLinkExtTable=_EtsysRs232CtsLinkExtTable_Object((1,3,6,1,4,1,5624,1,2,77,1,2,1))
if mibBuilder.loadTexts:etsysRs232CtsLinkExtTable.setStatus(_A)
_EtsysRs232CtsLinkExtEntry_Object=MibTableRow
etsysRs232CtsLinkExtEntry=_EtsysRs232CtsLinkExtEntry_Object((1,3,6,1,4,1,5624,1,2,77,1,2,1,1))
if mibBuilder.loadTexts:etsysRs232CtsLinkExtEntry.setStatus(_A)
class _EtsysRs232CtsLinkEnableState_Type(EnabledStatus):defaultValue=2
_EtsysRs232CtsLinkEnableState_Type.__name__=_C
_EtsysRs232CtsLinkEnableState_Object=MibTableColumn
etsysRs232CtsLinkEnableState=_EtsysRs232CtsLinkEnableState_Object((1,3,6,1,4,1,5624,1,2,77,1,2,1,1,1),_EtsysRs232CtsLinkEnableState_Type())
etsysRs232CtsLinkEnableState.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysRs232CtsLinkEnableState.setStatus(_A)
_EtsysRs232MibExtConformance_ObjectIdentity=ObjectIdentity
etsysRs232MibExtConformance=_EtsysRs232MibExtConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,77,2))
_EtsysRs232MibExtGroups_ObjectIdentity=ObjectIdentity
etsysRs232MibExtGroups=_EtsysRs232MibExtGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,77,2,1))
_EtsysRs232MibExtCompliances_ObjectIdentity=ObjectIdentity
etsysRs232MibExtCompliances=_EtsysRs232MibExtCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,77,2,2))
rs232PortEntry.registerAugmentions((_B,_F))
etsysRs232Vt100ExtEntry.setIndexNames(*rs232PortEntry.getIndexNames())
rs232PortEntry.registerAugmentions((_B,_G))
etsysRs232CtsLinkExtEntry.setIndexNames(*rs232PortEntry.getIndexNames())
etsysRs232MibExtVt100DsrGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,77,2,1,1))
etsysRs232MibExtVt100DsrGroup.setObjects(*((_B,_H),(_B,_I)))
if mibBuilder.loadTexts:etsysRs232MibExtVt100DsrGroup.setStatus(_A)
etsysRs232MibExtCtsLinkGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,77,2,1,2))
etsysRs232MibExtCtsLinkGroup.setObjects((_B,_J))
if mibBuilder.loadTexts:etsysRs232MibExtCtsLinkGroup.setStatus(_A)
etsysRs232MibExtCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,77,2,2,1))
etsysRs232MibExtCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:etsysRs232MibExtCompliance.setStatus(_A)
etsysRs232MibCtsExtCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,77,2,2,2))
etsysRs232MibCtsExtCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:etsysRs232MibCtsExtCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'etsysRs232MibExtMIB':etsysRs232MibExtMIB,'etsysRs232MibExtObjects':etsysRs232MibExtObjects,'etsysRs232MibExtVt100':etsysRs232MibExtVt100,'etsysRs232Vt100ExtTable':etsysRs232Vt100ExtTable,_F:etsysRs232Vt100ExtEntry,_H:etsysRs232Vt100DsrEnableState,_I:etsysRs232Vt100DsrTimeout,'etsysRs232MibExtCtsLink':etsysRs232MibExtCtsLink,'etsysRs232CtsLinkExtTable':etsysRs232CtsLinkExtTable,_G:etsysRs232CtsLinkExtEntry,_J:etsysRs232CtsLinkEnableState,'etsysRs232MibExtConformance':etsysRs232MibExtConformance,'etsysRs232MibExtGroups':etsysRs232MibExtGroups,_K:etsysRs232MibExtVt100DsrGroup,_L:etsysRs232MibExtCtsLinkGroup,'etsysRs232MibExtCompliances':etsysRs232MibExtCompliances,'etsysRs232MibExtCompliance':etsysRs232MibExtCompliance,'etsysRs232MibCtsExtCompliance':etsysRs232MibCtsExtCompliance})