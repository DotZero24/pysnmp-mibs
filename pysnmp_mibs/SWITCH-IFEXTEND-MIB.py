_C='rcIfindex'
_B='SWITCH-IFEXTEND-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rcIfExtend=ModuleIdentity((1,3,6,1,4,1,8886,6,1,20))
_RcIfExtendMib_ObjectIdentity=ObjectIdentity
rcIfExtendMib=_RcIfExtendMib_ObjectIdentity((1,3,6,1,4,1,8886,6,1,20,1))
_RcIfExtendTable_Object=MibTable
rcIfExtendTable=_RcIfExtendTable_Object((1,3,6,1,4,1,8886,6,1,20,1,1))
if mibBuilder.loadTexts:rcIfExtendTable.setStatus(_A)
_RcIfExtendEntry_Object=MibTableRow
rcIfExtendEntry=_RcIfExtendEntry_Object((1,3,6,1,4,1,8886,6,1,20,1,1,1))
rcIfExtendEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:rcIfExtendEntry.setStatus(_A)
_RcIfindex_Type=Integer32
_RcIfindex_Object=MibTableColumn
rcIfindex=_RcIfindex_Object((1,3,6,1,4,1,8886,6,1,20,1,1,1,1),_RcIfindex_Type())
rcIfindex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rcIfindex.setStatus(_A)
_RcIfDescription_Type=OctetString
_RcIfDescription_Object=MibTableColumn
rcIfDescription=_RcIfDescription_Object((1,3,6,1,4,1,8886,6,1,20,1,1,1,2),_RcIfDescription_Type())
rcIfDescription.setMaxAccess('read-write')
if mibBuilder.loadTexts:rcIfDescription.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rcIfExtend':rcIfExtend,'rcIfExtendMib':rcIfExtendMib,'rcIfExtendTable':rcIfExtendTable,'rcIfExtendEntry':rcIfExtendEntry,_C:rcIfindex,'rcIfDescription':rcIfDescription})