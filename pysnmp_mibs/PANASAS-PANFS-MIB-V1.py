if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
panProducts,=mibBuilder.importSymbols('PANASAS-ROOT-MIB','panProducts')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
panFs=ModuleIdentity((1,3,6,1,4,1,10159,1,3))
if mibBuilder.loadTexts:panFs.setRevisions(('2011-04-07 00:00',))
_PanEvents_ObjectIdentity=ObjectIdentity
panEvents=_PanEvents_ObjectIdentity((1,3,6,1,4,1,10159,1,3,1))
_PanSystem_ObjectIdentity=ObjectIdentity
panSystem=_PanSystem_ObjectIdentity((1,3,6,1,4,1,10159,1,3,2))
_PanBSet_ObjectIdentity=ObjectIdentity
panBSet=_PanBSet_ObjectIdentity((1,3,6,1,4,1,10159,1,3,3))
_PanVol_ObjectIdentity=ObjectIdentity
panVol=_PanVol_ObjectIdentity((1,3,6,1,4,1,10159,1,3,4))
_PanPerf_ObjectIdentity=ObjectIdentity
panPerf=_PanPerf_ObjectIdentity((1,3,6,1,4,1,10159,1,3,5))
mibBuilder.exportSymbols('PANASAS-PANFS-MIB-V1',**{'panFs':panFs,'panEvents':panEvents,'panSystem':panSystem,'panBSet':panBSet,'panVol':panVol,'panPerf':panPerf})