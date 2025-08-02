_C='current'
_B='read-only'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmITSwitchTech,=mibBuilder.importSymbols('HMIT-SMI','hmITSwitchTech')
hmITSwPortMIB,hmITSwPortmgrMIB=mibBuilder.importSymbols('HMIT-SW-PORT-MGR-MIB','hmITSwPortMIB','hmITSwPortmgrMIB')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hmITPortInfoMIB=ModuleIdentity((1,3,6,1,4,1,248,100,1,6,3,1,13,1))
if mibBuilder.loadTexts:hmITPortInfoMIB.setRevisions(('2010-01-08 17:00',))
class _HmITMaxPortNumOfBoard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HmITMaxPortNumOfBoard_Type.__name__=_A
_HmITMaxPortNumOfBoard_Object=MibScalar
hmITMaxPortNumOfBoard=_HmITMaxPortNumOfBoard_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,1,1),_HmITMaxPortNumOfBoard_Type())
hmITMaxPortNumOfBoard.setMaxAccess(_B)
if mibBuilder.loadTexts:hmITMaxPortNumOfBoard.setStatus(_C)
class _HmITStartPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HmITStartPortId_Type.__name__=_A
_HmITStartPortId_Object=MibScalar
hmITStartPortId=_HmITStartPortId_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,1,2),_HmITStartPortId_Type())
hmITStartPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:hmITStartPortId.setStatus(_C)
mibBuilder.exportSymbols('HMIT-SW-PORT-INFO-MIB',**{'hmITPortInfoMIB':hmITPortInfoMIB,'hmITMaxPortNumOfBoard':hmITMaxPortNumOfBoard,'hmITStartPortId':hmITStartPortId})