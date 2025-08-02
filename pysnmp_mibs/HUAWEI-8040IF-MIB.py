_E='DisplayString'
_D='ifIndex'
_C='IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mlsr,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','mlsr')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
hw8040If=ModuleIdentity((1,3,6,1,4,1,2011,2,33,7))
_Hw8040IfTable_Object=MibTable
hw8040IfTable=_Hw8040IfTable_Object((1,3,6,1,4,1,2011,2,33,7,1))
if mibBuilder.loadTexts:hw8040IfTable.setStatus(_A)
_Hw8040IfEntry_Object=MibTableRow
hw8040IfEntry=_Hw8040IfEntry_Object((1,3,6,1,4,1,2011,2,33,7,1,1))
hw8040IfEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:hw8040IfEntry.setStatus(_A)
_Hw8040IfInPerSecBits_Type=Integer32
_Hw8040IfInPerSecBits_Object=MibTableColumn
hw8040IfInPerSecBits=_Hw8040IfInPerSecBits_Object((1,3,6,1,4,1,2011,2,33,7,1,1,1),_Hw8040IfInPerSecBits_Type())
hw8040IfInPerSecBits.setMaxAccess(_B)
if mibBuilder.loadTexts:hw8040IfInPerSecBits.setStatus(_A)
_Hw8040IfOutPerSecBits_Type=Integer32
_Hw8040IfOutPerSecBits_Object=MibTableColumn
hw8040IfOutPerSecBits=_Hw8040IfOutPerSecBits_Object((1,3,6,1,4,1,2011,2,33,7,1,1,2),_Hw8040IfOutPerSecBits_Type())
hw8040IfOutPerSecBits.setMaxAccess(_B)
if mibBuilder.loadTexts:hw8040IfOutPerSecBits.setStatus(_A)
_Hw8040CRCIfInputErr_Type=Integer32
_Hw8040CRCIfInputErr_Object=MibTableColumn
hw8040CRCIfInputErr=_Hw8040CRCIfInputErr_Object((1,3,6,1,4,1,2011,2,33,7,1,1,3),_Hw8040CRCIfInputErr_Type())
hw8040CRCIfInputErr.setMaxAccess(_B)
if mibBuilder.loadTexts:hw8040CRCIfInputErr.setStatus(_A)
_Hw8040IfOutCollisions_Type=Integer32
_Hw8040IfOutCollisions_Object=MibTableColumn
hw8040IfOutCollisions=_Hw8040IfOutCollisions_Object((1,3,6,1,4,1,2011,2,33,7,1,1,4),_Hw8040IfOutCollisions_Type())
hw8040IfOutCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:hw8040IfOutCollisions.setStatus(_A)
class _Hw8040IfDescCfg_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_Hw8040IfDescCfg_Type.__name__=_E
_Hw8040IfDescCfg_Object=MibTableColumn
hw8040IfDescCfg=_Hw8040IfDescCfg_Object((1,3,6,1,4,1,2011,2,33,7,1,1,5),_Hw8040IfDescCfg_Type())
hw8040IfDescCfg.setMaxAccess('read-write')
if mibBuilder.loadTexts:hw8040IfDescCfg.setStatus(_A)
mibBuilder.exportSymbols('HUAWEI-8040IF-MIB',**{'hw8040If':hw8040If,'hw8040IfTable':hw8040IfTable,'hw8040IfEntry':hw8040IfEntry,'hw8040IfInPerSecBits':hw8040IfInPerSecBits,'hw8040IfOutPerSecBits':hw8040IfOutPerSecBits,'hw8040CRCIfInputErr':hw8040CRCIfInputErr,'hw8040IfOutCollisions':hw8040IfOutCollisions,'hw8040IfDescCfg':hw8040IfDescCfg})