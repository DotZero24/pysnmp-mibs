_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
panGlobalRegModule=ModuleIdentity((1,3,6,1,4,1,25461,1,1,1))
if mibBuilder.loadTexts:panGlobalRegModule.setRevisions(('2011-02-09 16:10',))
_PanRoot_ObjectIdentity=ObjectIdentity
panRoot=_PanRoot_ObjectIdentity((1,3,6,1,4,1,25461))
if mibBuilder.loadTexts:panRoot.setStatus(_A)
_PanReg_ObjectIdentity=ObjectIdentity
panReg=_PanReg_ObjectIdentity((1,3,6,1,4,1,25461,1))
if mibBuilder.loadTexts:panReg.setStatus(_A)
_PanModules_ObjectIdentity=ObjectIdentity
panModules=_PanModules_ObjectIdentity((1,3,6,1,4,1,25461,1,1))
if mibBuilder.loadTexts:panModules.setStatus(_A)
_PanMibs_ObjectIdentity=ObjectIdentity
panMibs=_PanMibs_ObjectIdentity((1,3,6,1,4,1,25461,2))
if mibBuilder.loadTexts:panMibs.setStatus(_A)
_PanCommonMib_ObjectIdentity=ObjectIdentity
panCommonMib=_PanCommonMib_ObjectIdentity((1,3,6,1,4,1,25461,2,1))
if mibBuilder.loadTexts:panCommonMib.setStatus(_A)
_PanSpecificMib_ObjectIdentity=ObjectIdentity
panSpecificMib=_PanSpecificMib_ObjectIdentity((1,3,6,1,4,1,25461,2,2))
if mibBuilder.loadTexts:panSpecificMib.setStatus(_A)
_PanProductsMibs_ObjectIdentity=ObjectIdentity
panProductsMibs=_PanProductsMibs_ObjectIdentity((1,3,6,1,4,1,25461,2,3))
if mibBuilder.loadTexts:panProductsMibs.setStatus(_A)
mibBuilder.exportSymbols('PAN-GLOBAL-REG',**{'panRoot':panRoot,'panReg':panReg,'panModules':panModules,'panGlobalRegModule':panGlobalRegModule,'panMibs':panMibs,'panCommonMib':panCommonMib,'panSpecificMib':panSpecificMib,'panProductsMibs':panProductsMibs})