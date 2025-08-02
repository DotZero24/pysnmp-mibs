_C='current'
_B='read-write'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cyACSMgmt,=mibBuilder.importSymbols('CYCLADES-ACS-MIB','cyACSMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cyACSAdm=ModuleIdentity((1,3,6,1,4,1,2925,4,4))
if mibBuilder.loadTexts:cyACSAdm.setRevisions(('2005-08-29 00:00','2002-09-20 00:00'))
class _CyACSSave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('nosave',0),('save',1)))
_CyACSSave_Type.__name__=_A
_CyACSSave_Object=MibScalar
cyACSSave=_CyACSSave_Object((1,3,6,1,4,1,2925,4,4,1),_CyACSSave_Type())
cyACSSave.setMaxAccess(_B)
if mibBuilder.loadTexts:cyACSSave.setStatus(_C)
class _CyACSSerialHUP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('norestartportslave',0),('restartportslave',1)))
_CyACSSerialHUP_Type.__name__=_A
_CyACSSerialHUP_Object=MibScalar
cyACSSerialHUP=_CyACSSerialHUP_Object((1,3,6,1,4,1,2925,4,4,2),_CyACSSerialHUP_Type())
cyACSSerialHUP.setMaxAccess(_B)
if mibBuilder.loadTexts:cyACSSerialHUP.setStatus(_C)
mibBuilder.exportSymbols('CYCLADES-ACS-ADM-MIB',**{'cyACSAdm':cyACSAdm,'cyACSSave':cyACSSave,'cyACSSerialHUP':cyACSSerialHUP})