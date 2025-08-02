_H='cpqSpecTrapID'
_G='cpqGenTrapID'
_F='cpqGenEntOIDStr'
_E='DisplayString'
_D='NotificationType'
_C='mandatory'
_B='read-only'
_A='CPQGEN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols('SNMPv2-MIB','sysName')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_D,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_D,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
_Compaq_ObjectIdentity=ObjectIdentity
compaq=_Compaq_ObjectIdentity((1,3,6,1,4,1,232))
_CpqGenUnreg_ObjectIdentity=ObjectIdentity
cpqGenUnreg=_CpqGenUnreg_ObjectIdentity((1,3,6,1,4,1,232,151))
_CpqGenComponent_ObjectIdentity=ObjectIdentity
cpqGenComponent=_CpqGenComponent_ObjectIdentity((1,3,6,1,4,1,232,151,2))
_CpqTrapVarBind_ObjectIdentity=ObjectIdentity
cpqTrapVarBind=_CpqTrapVarBind_ObjectIdentity((1,3,6,1,4,1,232,151,2,2))
class _CpqGenEntOIDStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqGenEntOIDStr_Type.__name__=_E
_CpqGenEntOIDStr_Object=MibScalar
cpqGenEntOIDStr=_CpqGenEntOIDStr_Object((1,3,6,1,4,1,232,151,2,2,1),_CpqGenEntOIDStr_Type())
cpqGenEntOIDStr.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqGenEntOIDStr.setStatus(_C)
_CpqGenTrapID_Type=Integer32
_CpqGenTrapID_Object=MibScalar
cpqGenTrapID=_CpqGenTrapID_Object((1,3,6,1,4,1,232,151,2,2,2),_CpqGenTrapID_Type())
cpqGenTrapID.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqGenTrapID.setStatus(_C)
_CpqSpecTrapID_Type=Integer32
_CpqSpecTrapID_Object=MibScalar
cpqSpecTrapID=_CpqSpecTrapID_Object((1,3,6,1,4,1,232,151,2,2,3),_CpqSpecTrapID_Type())
cpqSpecTrapID.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSpecTrapID.setStatus(_C)
cpqGenericUnregistered=NotificationType((1,3,6,1,4,1,232,0,99999))
cpqGenericUnregistered.setObjects(*((_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:cpqGenericUnregistered.setStatus('')
mibBuilder.exportSymbols(_A,**{'compaq':compaq,'cpqGenericUnregistered':cpqGenericUnregistered,'cpqGenUnreg':cpqGenUnreg,'cpqGenComponent':cpqGenComponent,'cpqTrapVarBind':cpqTrapVarBind,_F:cpqGenEntOIDStr,_G:cpqGenTrapID,_H:cpqSpecTrapID})